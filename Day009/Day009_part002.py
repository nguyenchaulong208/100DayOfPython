#Dictionaries: cho phép chúng ta nhóm lại vời nhau và gắn thẻ các phần thông tin liên quan
#syntax: {key: value}
#Ví dụ:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#print value của 1 key cụ thể thể trong dictonaries

print(thisdict["model"])

#Sửa giá trị trong dictionaries

thisdict["brand"] = "Ferrari"
print(thisdict)
#Thêm item mới vào dictionaries
thisdict["color"] = "Red"
print(thisdict)

#Tạo 1 dictionaries trống

emmty_dictionaries = {}

#Xóa hết các item trong dictionaries

thisdict = {}
print(thisdict)

#Lồng Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)