infile = r"C:\Users\ambas\OneDrive\Desktop\Coding Interview\log.txt" #Some path

important = []
keep_phrases = ["test","important","keep me"]

with open(infile) as f: #Defaults to read mode
    for line in f:
        print(line)
        for phrase in keep_phrases:
            if phrase in line:
                important.append(line.strip())
                break

print(important)

# parsed_data = []
  
# with open("example.logs","r") as file:
#     prev_time = ""
#     data = {}
#     for line in file:
#         time = line.split("[")[1].split("]")[0].split(" ")[0]
#         status_code = line.split('"')[2].split(" ")[1]
#         if prev_time != "":
#             if time == prev_time:
#                 data[time]["count"] = data[time]["count"] + 1
#                 if status_code in data[time]:
#                     data[time][status_code] = data[time][status_code] + 1
#                 else:
#                     data[time][status_code] = 1
#             else:
#                 prev_time = time
#                 parsed_data.append(data)
#                 data = {}
#                 data[time] = {"count": 1, status_code: 1}
#         else:
#             prev_time = time
#             data[time] = {"count": 1, status_code: 1}

# for i in parsed_data:
#     print(i)