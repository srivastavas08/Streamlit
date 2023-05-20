import streamlit as st

st.title("Title --> Hi There, Welcome to StreamLit Test")    # title
st.header('Header --> Streamlit')                            # Header
st.subheader('Subheader --> Streamlit')                      # subheader
st.text('Text --> Streamlit')                                # Text

st.subheader("Markdown")
st.markdown('# Hi')                                          # Markdown
st.markdown('## Hi')                                         # Markdown
st.markdown('### Hi')                                        # Markdown
st.markdown('#### Hi')                                       # Markdown
st.markdown('##### Hi')                                      # Markdown
st.markdown('Hi')                                            # Markdown


st.subheader("Alerts")
st.success('Success')                                       # Success
st.info('Information')                                      # Info
st.warning('Warning')                                       # Warning
st.error('Error')                                           # Error

st.subheader("Exception and Help")
exp = ZeroDivisionError('Division not possible with Zero') 
st.exception(exp)                                           # Exception

st.help(ZeroDivisionError)                                  # Help

st.subheader("Write")
st.write("Range(1,10)")                                     # Write
st.write(range(1,10))

st.write("1+2+3")
st.write(1+2+3)

st.subheader("Code")
st.code('x= 10 \n'                                          # Code
        'for i in range(x): \n'
                '\tprint(i)')

st.subheader("Checkbox")
st.checkbox('Male')                                         # Checkbox

if (st.checkbox('Adult')):                                  # Checkbox with Validation
    st.write("You're an Adult")



st.subheader("Radio Button")                                 # Radio Button
radioButton = st.radio('Select: ', ('Male', 'Female', 'Other'))
if (radioButton == 'Male'):
    st.write("You're a Male")
elif (radioButton == 'Female'):
    st.write("You're a Female")
elif (radioButton == 'Other'):
    st.write("You're an Other")
    
st.subheader("Select Box")                                  # Select Box
selectbox = st.selectbox("DataScience :", ['None','Data Analysis' , 'Web Scrapping', 
                                           'Machine Learning', 'Deep Learning',
                                           'Natural Language Processing', 'Computer Visison',
                                           'Image Processing'])

st.write("You have selected : ", selectbox)

st.subheader("MultiSelect Box")                                  # MultiSelect Box
multiselect = st.multiselect("DataScience :", ['Data Analysis' , 'Web Scrapping', 
                                           'Machine Learning', 'Deep Learning',
                                           'Natural Language Processing', 'Computer Visison',
                                           'Image Processing'])

st.write("You have selected : ", len(multiselect),' Courses')


st.subheader("Button")                                          # Button
if(st.button('click me')):
    st.write("Thanks for clicking me")
    
    
    
st.subheader('Slider')                                          # Slider
slider = st.slider('Select the volume : ', 0,100,step = 1)
st.write('The volume is :', slider)


    
st.subheader('Select SLider')                                   # SliderArea
slider = st.select_slider("Select your Mood : ", ['Sad' , 'Normal', 
                                           'Happy', 'Very Happy',
                                           'Happiest'])
st.write('Your mood is :', slider)



st.subheader("Text Input")                                      # Text Imput
name = st.text_input("Enter your Name:")
password = st.text_input("Enter your password:", type='password')
if (name):
    st.write(f"Hello!, {name}")
if (password):
    st.write("Your password is :", password)
    
    
    
st.subheader("Text Area")                                       # Text Area
textArea = st.text_area("Tell us something about yourself in 500 words:", max_chars=500)
if (textArea):
    st.write(textArea)
    
st.subheader("Input Number")                                    # Input Number
st.number_input("select your age :",18,110)

st.subheader("Input date")                                      #Input Date
st.date_input("Date :")

st.subheader("Input Time")                                      #Input Time
st.time_input("Time :")
    

