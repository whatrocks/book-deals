import ezgmail

def search_email():
    # Search for emails from "daily@publisherslunch.com" with the subject "Today's deals from PublishersMarketplace.com"
    threads = ezgmail.search("'Middle Grade Fiction' from:daily@publisherslunch.com subject:'Today's deals from PublishersMarketplace.com'")
    
    middle_grade_fiction_paragraphs = []
    
    # Iterate over the threads
    for thread in threads:
        # Get the latest message from the thread
        email = thread.messages[-1]
        
        # Get the body of the email as plain text
        email_body = email.body
       # print(email)
        # Get the body of the email as plain text
        # email_body = email.originalBody
        
        # Split the body into lines
        lines = email_body.split('\n')
        
        # Flag to check if we're in the Middle Grade Fiction section
        in_middle_grade_section = False
        
        # Iterate over the lines
        for line in lines:
#            print(line)
            if line.startswith("**Middle Grade Fiction**"):
                # We've found the start of the Middle Grade Fiction section
                in_middle_grade_section = True
            elif line.startswith("**"):
                # We've found the end of the Middle Grade Fiction section
                if in_middle_grade_section:
                    break
                else:
                    continue
            elif in_middle_grade_section:
                # We're in the Middle Grade Fiction section, so add the line to our list
                middle_grade_fiction_paragraphs.append(line)
    return middle_grade_fiction_paragraphs

if __name__ == '__main__':
    middle_grade_paragraphs = search_email()
    print(len(middle_grade_paragraphs))
    for paragraph in middle_grade_paragraphs:
        print(paragraph)
