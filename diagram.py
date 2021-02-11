from diagrams import Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.database import DynamodbTable
from diagrams.aws.network import APIGateway

with Diagram("Calendar Events", show=False, direction="TB"):

    APIGateway("calendar events api") >> Lambda("calendar events") >> DynamodbTable("calendar events")
