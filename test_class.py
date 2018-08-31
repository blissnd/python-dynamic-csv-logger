from Dynamic_CSV_Logger import *

class TestClass:
	def __init__(self, logger):
		self.logger = logger
		print "I'm inside the __init__"
		logger.log_current_status(self, {'Message with \nnewline':'In __init__'})

	def another_function(self):
		print "I'm inside another function"
		logger.log_current_status(self, {'Message with \nnewline':'In \nanother_function'})


def outside_function(logger):
	print "I'm not inside any class"
	class_name = "Not inside a class!"
	logger.log_current_status(None, {'Message with "double quotes"':'"In, outside_\nfunction"','custom_var':class_name})

#########################################################################

logger = Logger()

outside_function(logger)
test_class_obj = TestClass(logger)

logger.log_current_status(None, {'Message with "double quotes"':'"In MAIN"'})

test_class_obj.another_function()
outside_function(logger)

logger.print_to_csv_file()

