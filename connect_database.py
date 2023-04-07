from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
  'secure_connect_bundle': 'D:\Data Science\Projects\mushroomClassification\code\Mushroom Classifier\secure-connect-test.zip'
}
auth_provider = PlainTextAuthProvider('NQcbFgyywnmQxWKjhouSIAdK', '5y-0EA5KEkNY6GLJMEJf0g.6xN,X9ABghq2JU9bDAw.0kUqFMylD6+vos_,IuhAc_yz7PeZOxlnrEcrCWRlj8D2wZi0UnC-195tWer8kHPg7jlFGYc_1ZIAX6aqJ0NZ1')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
  print("sucess"+row[0])
else:
  print("An error occurred.")