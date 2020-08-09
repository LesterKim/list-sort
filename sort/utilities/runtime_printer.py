from datetime import datetime


def runtime_printer(function):
	def runtime_printing_function(*args, **kwargs):
		start = datetime.now()
		result = function(*args, **kwargs)
		end = datetime.now()
		runtime = end - start

		print(runtime)

		return result


	return runtime_printing_function