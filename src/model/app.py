import gradio as gr
import os
from huggingface_hub import InferenceClient

# Retrieve the API key from the Hugging Face Secrets
api_key = os.getenv("HF_API_KEY")

# Initialize the Inference Client securely
client = InferenceClient(
    provider="hf-inference",
    api_key=api_key,  # Using the secret instead of hardcoding
)

# Your dataset (Liver Cancer Information)
context = """📘 Liver Cancer – Cleaned Text for NLP Use
Overview
Liver cancer originates in the liver cells. The liver, a football-sized organ, is located in the
upper right portion of the abdomen beneath the diaphragm and above the stomach.
The most common liver cancer type is hepatocellular carcinoma (HCC). Other forms
include intrahepatic cholangiocarcinoma and hepatoblastoma. Liver metastases are more
common than primary liver cancers.
🔍 Causes
Liver cancer is often caused by mutations in liver cell DNA, leading to uncontrolled
growth and tumors.
Sometimes linked to chronic hepatitis B or C infections.
It may also occur without any known underlying disease.
 Risk Factors
Chronic infection with HBV (hepatitis B) or HCV (hepatitis C)
Cirrhosis (scarring of the liver)
Inherited liver diseases (e.g., hemochromatosis, Wilson’s disease)
Diabetes
Nonalcoholic fatty liver disease (NAFLD)
Exposure to aatoxins from moldy food (grains, nuts)
Excessive alcohol consumption
🧪 Diagnosis
Alpha-fetoprotein (AFP) is a common biomarker
CT scans, MRI, and ultrasound are used for imaging
💊 Treatment Options
Surgical resection
Liver transplantation
Targeted therapies (e.g., sorafenib)
Immunotherapy
Research is exploring TP53 mutations for personalized medicine
🧬 Symptoms
Weight loss
Loss of appetite
Upper abdominal pain
Nausea and vomiting
Weakness and fatigue
Abdominal swelling
Jaundice (yellow skin and eyes)
White, chalky stools
✅ Prevention
Reduce Cirrhosis Risk
Drink alcohol moderately (max 1 drink/day for women, 2 for men)
Maintain a healthy weight through diet and exercise
Prevent Hepatitis B & C
Get vaccinated against HBV
Avoid IV drug use or use sterile needles
Practice safe sex
Choose clean, professional facilities for tattoos and piercings
Screening
Screening (blood tests and ultrasound every 6 months) may be advised for high-risk
groups (e.g., hepatitis B/C, cirrhosis)."""

# Function to send user questions to the model with context
def ask_model(question):
    full_prompt = f"Context: {context}\n\nUser: {question}\n\nAssistant:"
    response = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.1",
        messages=[{"role": "user", "content": full_prompt}],
        max_tokens=500,
    )
    return response.choices[0].message["content"]

# Build the Gradio Interface
with gr.Blocks(fill_height=True) as demo:
    with gr.Sidebar():
        gr.Markdown("# Inference Provider")
        gr.Markdown("This Space showcases the mistralai/Mistral-7B-Instruct-v0.1 model, now fine-tuned with Liver Cancer Information.")
        gr.Markdown("Ask questions related to liver cancer and get AI-generated answers.")
        button = gr.LoginButton("Sign in")
    
    gr.Markdown("### Ask the AI about Liver Cancer:")
    user_input = gr.Textbox(label="Your Question", placeholder="Type your question here...")
    submit_button = gr.Button("Ask")
    output_text = gr.Textbox(label="AI's Response")

    submit_button.click(ask_model, inputs=user_input, outputs=output_text)

# Launch the Gradio app
demo.launch()
