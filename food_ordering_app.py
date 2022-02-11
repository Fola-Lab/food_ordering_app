#IMPORT MODULE
import streamlit as st

# Date Input
import datetime 

the_time = datetime.datetime.now().strftime('%y-%m-%d %H:%M')

st.write(the_time)

from PIL import Image
img = Image.open("foodbanner.png")

# display image using streamlit
st.image(img, width=700)

# give a title to our app
st.title('WELCOME TO SUPER TASTY NUTRIMEAL')

foodordered_history={}
myorder = []

user = st.sidebar.text_input('Username')


order = st.sidebar.radio(' WOULD YOU LIKE TO ORDER, '+ user.upper()+ '?', ('Yes', 'No'))
if order == 'Yes':
    st.success("Proceed")
          
    st.write('\nPlease, kindly check the Menu list: \n')
    
    #Layout
    col1, col2 = st.columns(2)
        
    with col1:
        menu = st.selectbox('MENU', [' ','fried rice','jollof rice','abacha','beans','pottage',
                                 'moinmoin','bottle-water','smoothie','juice','fruitwine'])

        menu_price =st.selectbox('PRICE', [' ',200,250,400,500,1000, 1500]) 
        Delivery_mode = st.sidebar.radio('DELIVERY MODE', ['Location', 'Physical pick up', 'Served'])
        if Delivery_mode =='Location':
            Address= st.text_input('Enter your Address')
            Date= st.date_input('Delivery Date')
        
        elif Delivery_mode =='Physical pick up':
            Date= st.date_input('Pick up date')
            Pickup_time = st.time_input('Time of pick up')
            
        elif Delivery_mode =='Served':
            table_num = st.text_input('Enter your Table Number')
            if table_num == '1':
                st.write('Your order will be ready in 2 minutes')
            elif table_num == '2':
                st.write('Your order will be ready in 3 minutes')
            elif table_num == '3':
                st.write('Your order will be ready in 4 minutes')
            elif table_num == '4':
                st.write('Your order will be ready in 5 minutes')
            elif table_num == '5':
                st.write('Your order will be ready in 6 minutes')
            else:
                st.write('Table not found')
                                                
    with col2:
        num_ordered = st.number_input('Number of Order')
        order_price = st.number_input('Amount')
        #store item ordered in dict
        foodordered_history = {'Quantity': num_ordered, 'Price':order_price}
        myorder.append(foodordered_history)
       
        
        if st.button("Add Order"):
            
            try:
                st.success("Order Added Successfully: {}".format(order))
            except:
                st.text("You have not enter some value for your height")
            
        Total_Order = 0
        
        for key, orders in enumerate(myorder):
            Order_total = orders['Quantity'] * orders['Price']
            Total_Order = Total_Order + Order_total
       
    if(st.button('Calculate Total Order')):
        st.text('Total_Order : $%.2f' % Total_Order)
        st.success('Success')
        
else:
    st.write("Have a nice day")
    st.warning("Exit")



hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)