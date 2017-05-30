import read
from dateutil.parser import parse

def parse_submission_time(submission_time, property):
	submission_datetime = parse(submission_time)
	DOW_dict = {
				0: "Mon",
				1: "Tue",
				2: "Wed",
				3: "Thu",
				4: "Fri",
				5: "Sat",
				6: "Sun"
				}
	property_dict = {
					"year": submission_datetime.year,
					"month": submission_datetime.month,
					"DOW": DOW_dict[submission_datetime.weekday()],
					"hour": submission_datetime.hour
					}
	DOW_dict = {
				0: "Mon",
				1: "Tue",
				2: "Wed",
				3: "Thu",
				4: "Fri",
				5: "Sat",
				6: "Sun"
				}
	return property_dict[property]
	
if __name__=="__main__":
	hn = read.load_data()
	hn["submission_year"] = hn["submission_time"].apply(lambda x: parse_submission_time(x, "year"))
	print("\nSubmission YEARS in descending order of counts:", hn["submission_year"].value_counts(sort=True), sep='\n')
	hn["submission_month"] = hn["submission_time"].apply(lambda x: parse_submission_time(x, "month"))
	print("\nSubmission MONTHS in descending order of counts:\n", hn["submission_month"].value_counts(sort=True), sep='\n')
	hn["submission_DOW"] = hn["submission_time"].apply(lambda x: parse_submission_time(x, "DOW"))
	print("\nSubmission WEEKDAYS in descending order of counts:\n", hn["submission_DOW"].value_counts(sort=True), sep='\n')
	hn["submission_hour"] = hn["submission_time"].apply(lambda x: parse_submission_time(x, "hour"))
	print("\nSubmission HOURS in descending order of counts:\n", hn["submission_hour"].value_counts(sort=True), sep='\n')

