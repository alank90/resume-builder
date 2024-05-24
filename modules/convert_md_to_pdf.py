import requests

def convert(markdown_content, resume_file, engine="weasyprint"):
    # Define CSS styles for the PDF
    css_file = """
                body{
                    padding: 0px;
                    margin:0px;
                }
                h1 {
                color: MidnightBlue;
                margin:0px;
                padding:0px;

                }
                h3{
                    color: MidnightBlue;
                    padding-bottom:0px;
                    margin-bottom:0px;
                }
                li{
                    margin-top:5px;
                }

                """

    # API endpoint for converting Markdown to PDF
    url_address = "https://md-to-pdf.fly.dev"

    # Data to be sent in the POST request
    data = {
        'markdown': markdown_content,
        'css': css_file,
        'engine': engine
    }

    # Send a POST request to the API
    response = requests.post(url_address, data=data)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Save the generated PDF to a file
        resume_file.write(response.content)
        print(f"PDF saved to {resume_file}")
    else:
        print(f"Error {response.status_code}: {response.text}")
