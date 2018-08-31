import imp
import inspect
import sys
import datetime
import re

class Logger:
	logger_headers = []
	logger_row_list = []
	
	########################################################################
	
	def __init__(self):
		self.worker_thread_ref = 0
		
		self.filename = ""
		self.function_name = ""
		self.class_name = ""
		
		self.logger_headers.append('Time')
		self.logger_headers.append('Filename')
		self.logger_headers.append('Class')
		self.logger_headers.append('Function')
		
	# End Function
	########################################################################
	
	def log_current_status(self, object_instance, param_dict):
		
		filename = inspect.stack()[1][1]
		function_name = inspect.stack()[1][3]
		class_name = object_instance.__class__.__name__
		
		logger_row = []
		logger_row.append(str(datetime.datetime.now()))
		logger_row.append(filename)
		logger_row.append(class_name)
		logger_row.append(function_name)
		
		for key,val in param_dict.items():
			
			key = re.sub('"', '""', key)
			val = re.sub('"', '""', val)
			
			if key not in self.logger_headers:
				self.logger_headers.append(key)
			# End If
			
			field_index = self.logger_headers.index(key)
			
			while (len(logger_row) -1) < field_index:
				logger_row.append('')
			# End While
			
			logger_row[field_index] = val
		# End For
		
		self.logger_row_list.append(logger_row)
		
	# End Function
	########################################################################
	
	def print_to_csv_file(self):
		
		output_file_handle = open("csv_log.csv", "w")
		
		field_count = 1
		
		for header_field in self.logger_headers:
			output_file_handle.write('"' + header_field + '"')
			
			if field_count < len(self.logger_headers):
				output_file_handle.write(',')
			else:
				output_file_handle.write('\n')
			# End If
			field_count = field_count + 1
		# End For
		
		for row in self.logger_row_list:
			field_count = 1
			
			for field in row:				
				output_file_handle.write('"' + field + '"')
				
				if field_count < len(row):
					output_file_handle.write(',')
				else:
					output_file_handle.write('\n')
				# End If
				
				field_count = field_count + 1
			# End For
		# End For
		
		output_file_handle.close()
	
	# End Function
	########################################################################
	
# End Class

