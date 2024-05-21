import requests


def convert_markdown_to_pdf(markdown_content, resume_file="Resume.pdf", engine="weasyprint"):
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
    
