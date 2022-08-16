import streamlit as st
#import openpyxl as pxl
#import panda as pd


#login = pd.read_excel('login.xlsx')
#exp = pxl.load_workbook('login.xlsx')
#sheet = exp['Sheet']
#sheet['D1'] = 'hii'

from streamlit.proto.Button_pb2 import Button 
from src import text
def main():

      st.title("Waste Management App")
      menu = ["Home","Login","Signup","text"]
      choice = st.sidebar.selectbox("Menu",menu)
      
      if choice== "text":
          text.textFm()
          

      if choice == "Home":

          st.subheader("Home") 
          st.title("GARBAGE MANAGEMENT APP")
          from PIL import Image
          img = Image.open("save earth from garbage.jpeg") 
          st.image(img,width=600)
          st.subheader("About Us:")
          st.text("The aim of the project is to provide a better solution to waste management.")
          st.text("Instead of dumping waste to another area,") 
          st.text("this app proposes to transport waste to those who require it for useful purposes.") 
          st.text("Hence the 'bekaar' is delivered to the companies who 'sweekar' it.")
          st.subheader("Importance")
          st.subheader("Working")
          st.text("Our website involves a total of 3 steps:")
          st.text("1)Collection of waste from the user. The waste collected is divided in 5 Categories : ")
          st.text("Paper, Plastic, Organic, Glass, Metal. The users can submit waste that")
          st.text("2)The delivery of the waste from the user to the company where the latter can order")
          st.text("the waste materials they want to use/process, right to their doorstep.")

          st.text("3)Utilisation of Waste : The company now, uses the waste by amicably collecting it,")
          st.text("profusely processing it and efficiently recycling it. (for example: A packaging company ")
          st.text(" may require old newspaper/books, an animal farm may require organic wastes and so on.)")
          st.sidebar.header("Contact Us:xxxxxxxxxxx")
          st.sidebar.header("Contact Us:xxxxxxxxxxx@gmai.com")










      elif choice == "Login":
          st.subheader("Login Section")
          username = st.sidebar.text_input("User Name")
          password = st.sidebar.text_input("password",type='password')
          if st.sidebar.checkbox('Login'):
              st.success("Logged In as {}".format(username))
              task = st.selectbox("Role",["Role","Waste Giver","Waste Taker"])
              if task =="Role":
                  st.subheader("Add your Role")
              elif task == "Waste Giver":
                    st.subheader("Waste Giver")
                   #user_name = st.write("Enter your name")
                    Name_ = st.text_input("Enter your Name")
                    email_id = st.text_input("Enter your email_id")
                    contact_no = st.text_input("Enter your contact no")
                    address = st.text_input("Enter your address")
                    #type = st.text_input("Enter type of Waste")
                    type= st.selectbox("Type",["type","Municipal solid waste","Hazardous waste","Biodegreadable waste","E-waste","Household hazardous waste"])




              elif task == "Waste Taker":
                    st.subheader("Waste Taker")
                    compony_Name = st.text_input("Enter your Compony/Industry Name")
                    email_id = st.text_input("Enter your email_id")
                    contact_no = st.text_input("Enter your contact no")
                    address = st.text_input("Enter your address")
                    type= st.selectbox("Type of waste you want for recycle",["type","Municipal solid waste","Hazardous waste","Biodegreadable waste","E-waste","Household hazardous waste"])  






      elif choice == "Signup":
          st.subheader("Create New Account")
          new_user = st.text_input("Username")
          new_password = st.text_input("Password",type='password')
          
          
          if  st.button("signup"):
              st.success("You have successfully created an account")
              st.info("Goto Login Menu to Login")  
               


if __name__ == '__main__':
    main()      

