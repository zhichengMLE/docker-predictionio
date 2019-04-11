"""
Import sample data for recommendation engine
"""

import predictionio
import argparse
import random
import datetime
import pytz

RATE_ACTIONS_DELIMITER = ","
PROPERTIES_DELIMITER = ":"
SEED = 1


def import_events(client, file):
  f = open(file, 'r')
  random.seed(SEED)
  count = 0
  # year, month, day[, hour[, minute[, second[
  #event_date = datetime.datetime(2015, 8, 13, 12, 24, 41)
  now_date = datetime.datetime.now(pytz.utc) # - datetime.timedelta(days=2.7)
  current_date = now_date
  event_time_increment = datetime.timedelta(days= -0.8)
  available_date_increment = datetime.timedelta(days= 0.8)
  event_date = now_date - datetime.timedelta(days= 2.4)
  available_date = event_date + datetime.timedelta(days=-2)
  expire_date = event_date + datetime.timedelta(days=100)
  print("Importing data...")

  for line in f:
    data = line.rstrip('\r\n').split(RATE_ACTIONS_DELIMITER)
    # For demonstration purpose action names are taken from input along with secondary actions on
    # For the UR add some item metadata

    if (data[1] != "$set"):
      client.create_event(
        event=data[1],
        entity_type="user",
        entity_id=data[0],
        target_entity_type="item",
        target_entity_id=data[2],
        event_time = current_date
      )
      print("Event: " + data[1] + " entity_id: " + data[0] + " target_entity_id: " + data[2] + \
            " current_date: " + current_date.isoformat())
    elif (data[1] == "$set"):  # must be a set event
      properties = data[2].split(PROPERTIES_DELIMITER)
      prop_name = properties.pop(0)
      prop_value = properties if not prop_name == 'defaultRank' else float(properties[0])
      client.create_event(
        event=data[1],
        entity_type="item",
        entity_id=data[0],
        event_time=current_date,
        properties={prop_name: prop_value}
      )
      print("Event: " + data[1] + " entity_id: " + data[0] + " properties/"+prop_name+": " + str(properties) + \
          " current_date: " + current_date.isoformat())
    count += 1
    current_date += event_time_increment

  items = ["4096",
"4097",
"4098",
"4099",
"4001",
"4002",
"4003",
"4004",
"4005",
"4006",
"4007",
"4008",
"4009",
"4010",
"4011",
"4012",
"4013",
"4014",
"4016",
"4017",
"4018",
"4019",
"4020",
"4021",
"4022",
"4023",
"4024",
"4025",
"4026",
"4027",
"4028",
"4029",
"4030",
"4031",
"4032",
"4033",
"4034",
"4035",
"4036",
"4037",
"4038",
"4039",
"4040",
"4041",
"4042",
"4043",
"4044",
"4045",
"4046",
"4047",
"4048",
"4049",
"4050",
"4051",
"4052",
"4053",
"4054",
"4055",
"4056",
"4057",
"4058",
"4059",
"4060",
"4061",
"4062",
"4063",
"4064",
"4065",
"4066",
"4067",
"4068",
"4069",
"4070",
"4071",
"4072",
"4073",
"4074",
"4075",
"4076",
"4077",
"4078",
"4079",
"4080",
"4081",
"4082",
"4083",
"4084",
"4085",
"4086",
"4087",
"4088",
"4090",
"4091",
"4092",
"4093",
"4094",
"4095"]
  print("All items: " + str(items))
  for item in items:

    client.create_event(
      event="$set",
      entity_type="item",
      entity_id=item,
      properties={"expires": expire_date.isoformat(),
                  "available": available_date.isoformat(),
                  "date": event_date.isoformat()}
    )
    print("Event: $set entity_id: " + item + \
            " properties/availableDate: " + available_date.isoformat() + \
            " properties/date: " + event_date.isoformat() + \
            " properties/expireDate: " + expire_date.isoformat())
    # expire_date += available_date_increment
    # event_date += available_date_increment
    # available_date += available_date_increment
    count += 1

  f.close()
  print("%s events are imported." % count)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    description="Import sample data for recommendation engine")
  parser.add_argument('--access_key', default='invald_access_key')
  parser.add_argument('--url', default="http://localhost:7070")
  parser.add_argument('--file', default="./data/nlt-data.txt")

  args = parser.parse_args()
  print(args)

  client = predictionio.EventClient(
    access_key=args.access_key,
    url=args.url,
    threads=5,
    qsize=500)
  import_events(client, args.file)
