from diagrams import Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.database import DynamodbTable
from diagrams.aws.integration import SNS
from diagrams.aws.network import APIGateway

with Diagram("Calendar Events", show=False, direction="TB"):

    events = Lambda("calendar events")
    topic = SNS("calendar topic")

    APIGateway("calendar events api") >> events >> DynamodbTable("calendar events") >> events
    events >> topic
