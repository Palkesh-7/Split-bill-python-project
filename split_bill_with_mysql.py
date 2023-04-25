import mysql.connector

# Establish a connection to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="india@123",
    database="split_bill"
)

# Create a cursor object
cursor = db.cursor()


def show_group_name():
  query = 'SHOW TABLES'

  cursor.execute(query)

  results = cursor.fetchall()

  for index,group_name in enumerate(results):

    print(index,"-",group_name)

def create_group():
  group_name = input("Enter Your group name : ")
  number_of_member = int(input("Enter Number of member :"))
  member_list = []
  for i in range(number_of_member):
    print("Enter ",i+1," member name")
    member_list.append(input(":->" ))
  query = 'CREATE TABLE '+ group_name + "("
  for i in range(number_of_member-1):
    query = query + member_list[i] + " FLOAT, "
  query = query + member_list[-1] + " FLOAT);"
  print(query)
  cursor.execute(query)
  print("Group is Created !")


def select_group_name():
  return input("Enter Selected Group Name : ")

def split_an_expense():
  show_group_name()
  group_name = select_group_name()
  amount = float(input("Total : "))
  split_between_names = []
  member_count = int(input("Enter number of people : "))
  for i in range(member_count):
    print("Enter ",i+1," member name")
    split_between_names.append(input(":-> "))
  equal_split = round(amount/member_count,2)
  query = "INSERT INTO " + group_name + " ("
  for i in range(member_count-1):
    query = query + split_between_names[i] + ","
  query = query + split_between_names[-1]+")"+ " VALUE("
  print(equal_split)
  print(query)
  for k in range(member_count-1):
    query = query + str(equal_split) + "," 
  query = query + str(equal_split) + ");"
  print(query)
  cursor.execute(query)
  db.commit()
  print("value added !")



# def expense():
#   pass

if __name__ == "__main__":
  # create_group()
  split_an_expense()
  cursor.close()