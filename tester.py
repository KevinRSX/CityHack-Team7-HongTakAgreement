import starwatch
import starwatch.toxml

starwatch.toxml.toxml("tester.xml", "../CityU-Hackathon-2019/Testing/67/*.pdf")
# res = starwatch.extract_entity("tester.xml")
# print(res)
res = starwatch.extract_auditor("tester.xml")
print(res)
