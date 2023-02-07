import ezgmail

def search_email():
    # Search for emails from "daily@publisherslunch.com" with the subject "Today's deals from PublishersMarketplace.com"
    emails = ezgmail.search("from:daily@publisherslunch.com subject:'Today's deals from PublishersMarketplace.com'")
    
    middle_grade_fiction_paragraphs = []
    
    # Iterate over the emails
    for email in emails:
        # Get the body of the email as plain text
        email_body = email.body
        
        # Split the body into lines
        lines = email_body.split('\n')
        
        # Flag to check if we're in the Middle Grade Fiction section
        in_middle_grade_section = False
        
        # Iterate over the lines
        for line in lines:
            if line == "Middle Grade Fiction:":
                # We've found the start of the Middle Grade Fiction section
                in_middle_grade_section = True
            elif line == "":
                # We've found the end of the Middle Grade Fiction section
                break
            elif in_middle_grade_section:
                # We're in the Middle Grade Fiction section, so add the line to our list
                middle_grade_fiction_paragraphs.append(line)
    
    return middle_grade_fiction_paragraphs

if __name__ == '__main__':
    middle_grade_paragraphs = search_email()
    for paragraph in middle_grade_paragraphs:
        print(paragraph)
