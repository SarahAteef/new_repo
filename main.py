from jinja2 import Environment , FileSystemLoader
import yaml

input("Welcome in our script")
User_input = input("Please choose what's protocol you want to apply Bgp or Ospf ")
if User_input == "Bgp":
  with (open("bgp.yml") as file):
      data= yaml.full_load(file)
      env = Environment(loader=FileSystemLoader('.'))
      temp = env.get_template("bgp.j2")
      Render = temp.render(int=data)
      print(Render)


elif User_input == "Ospf" :
    with open("ospf.yml") as file:
        data = yaml.full_load(file)



else :
    input('You should choose one protocol ')


























