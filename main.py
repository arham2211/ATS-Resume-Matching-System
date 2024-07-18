import streamlit as st
import os
import pdf2image
from dotenv import load_dotenv
import base64
import openai
import tempfile
load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_gemini_response(prompt, pdf_content_base64):
    response = client.chat.completions.create(
        model='gpt-4o',
        response_format={"type": "text"},
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": f"{prompt}"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{pdf_content_base64}"
                        }
                    }
                ]
            }
        ],
        max_tokens=500,
    )
    return response.choices[0].message.content

def pdf_to_images(pdf_path):
    # Ensure the output directory exists
    output_dir = r'D:\Percentages_Matches'
    
    # Convert PDF to images
    images = pdf2image.convert_from_path(pdf_path, poppler_path=r'poppler-24.02.0\Library\bin')
    
    # Save images to the specified directory
    for i, image in enumerate(images):
        image_path = os.path.join(output_dir, f"page_{i + 1}.jpeg")
        image.save(image_path, 'JPEG')
        print(f"Saved {image_path}")

def images_to_base64(image_dir):
    base64_images = []
    
    # Loop through all image files in the directory
    for image_file_name in os.listdir(image_dir):
        if image_file_name.endswith(".jpeg"):  # Ensure we're working with JPEG images
            image_path = os.path.join(image_dir, image_file_name)
            
            # Read and encode the image
            with open(image_path, 'rb') as image_file:
                image_base64 = base64.b64encode(image_file.read()).decode('utf-8')
                base64_images.append(image_base64)
    
    # Concatenate all base64 strings into one
    concatenated_base64 = "".join(base64_images)
    return concatenated_base64

# Streamlit App

st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text = st.text_area("Job Description: ", key="input")
user_input = st.text_input("How many top resume You need", key = "input1")

uploaded_files = st.file_uploader("Upload Your Resumes...", type="pdf", accept_multiple_files=True)

if uploaded_files is not None:
    st.write("PDFs Uploaded Successfully")

submit3 = st.button("Percentage Match")

input_prompt3 = f"""
You are expert in extracting information from a CV or resume and then As a skilled ATS (Applicant Tracking System) scanner 
with a deep understanding of ATS functionality, your task is to evaluate the provided resume against the given job 
description.

Compare the resume wit this given job description and with nothing else
============
{input_text}
============

Please provide the percentage of match between the resume and the job description based on the missing 
keywords.
The output should be only the percentage match between them
Percentage Match:
"""

if submit3:
    if uploaded_files is not None:
        matches_dict = {}
        for uploaded_file in uploaded_files:
            try:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                    temp_file.write(uploaded_file.read())
                    temp_pdf_path = temp_file.name
            except Exception as e:
                st.error(f"Error processing file {uploaded_file.name}: {str(e)}")
                continue
            
            # Call the function to convert the PDF to images
            pdf_to_images(temp_pdf_path)
            image_dir = r'D:\Percentages_Matches'  # Example directory, adjust as needed
            pdf_content = images_to_base64(image_dir)
            response = get_gemini_response(input_prompt3, pdf_content)

            matches_dict[uploaded_file.name] = response
            
        sorted_matches = sorted(matches_dict.items(), key=lambda item: item[1], reverse=True)
        
        # Convert user_input to integer
        try:
            user_input = int(user_input)
        except ValueError:
            st.error("Please enter a valid number for how many top matches to display.")
            user_input = 3  # Default to 3 if user_input is invalid
        
        # Print the top matches
        st.subheader(f"Top {user_input} Matches:")
        for i, (filename, percentage) in enumerate(sorted_matches[:user_input]):
            st.write(f"{i+1}. {filename}: {percentage}")

    else:
        st.write("Please upload the resumes")