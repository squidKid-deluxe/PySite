"""
    A module that takes python definitions and
    writes HTML script out of settings the user
    specifies.
"""
def file_name(file_n="default.html"):
    """
        Creating the html file.
    """
    handle = open(file_n, "w")
    handle.close()
    return file_n

def clear(file_n):
    """
        Clearing the html file.
    """
    # open file
    handle = open(file_n, "w")
    # clear file
    handle.write("")
    # close file
    handle.close()

def css(file_n,
        background="white",
        parafront="black",
        paraback="white",
        divback="gray",
        div="black",
        header_c="black",
        link_color="red"):
    """
        Creates the CSS of the HTML script.
        NOTE: this definition can also be used, alone,
        to create external CSS
    """
    # open file
    handle = open(file_n, "a")
    # write HTML that begins CSS
    handle.write("<html>\n\t<head>\n\t\t<style>\n\n\t\t\t")
    # write CSS that handles background color for the main text body
    handle.write("body {\n\t\t\t\tbackground-color: " + background + ";\n\t\t\t}\n\n\t\t\t")
    # write CSS that handles colors for the paragraphs
    handle.write(
        "p {\n\t\t\t\tbackground-color:"
        + paraback
        + ";\n\t\t\t\tcolor:"
        + parafront
        + ";\n\t\t\t}\n\t\t\t"
    )
    # write CSS that handles colors for the divisions
    handle.write(
        "div {\n\t\t\t\tbackground-color:"
        + divback
        + ";\n\t\t\t\tcolor:"
        + div
        + ";\n\t\t\t}\n\t\t\t"
    )
    # write CSS that handles foreground color for the links
    handle.write("a {\n\t\t\t\tcolor:" + link_color + ";\n\t\t\t}\n\t\t\t")
    # write CSS that handles foreground color for the different size headers
    handle.write("h1 {\n\t\t\t\tcolor:" + header_c + ";\n\t\t\t}\n\t\t\t")
    handle.write("h2 {\n\t\t\t\tcolor:" + header_c + ";\n\t\t\t}\n\t\t\t")
    handle.write("h3 {\n\t\t\t\tcolor:" + header_c + ";\n\t\t\t}\n\t\t\t")
    handle.write("h4 {\n\t\t\t\tcolor:" + header_c + ";\n\t\t\t}\n\t\t\t")
    handle.write("h5 {\n\t\t\t\tcolor:" + header_c + ";\n\t\t\t}\n\t\t\t")
    handle.write("h6 {\n\t\t\t\tcolor:" + header_c + ";\n\t\t\t}\n\t\t\t")
    handle.write("h7 {\n\t\t\t\tcolor:" + header_c + ";\n\t\t\t}\n\t\t\t")
    handle.write("h8 {\n\t\t\t\tcolor:" + header_c + ";\n\t\t\t}\n\t\t\t")
    handle.write("h9 {\n\t\t\t\tcolor:" + header_c + ";\n\t\t\t}\n\t\t\t")
    # write HTML that ends CSS
    handle.write("</style>\n\t</head>\n</html>\n\n")
    # close file
    handle.close()

def paragraph(file_n, text="\n"):
    """
        Creates paragraphs.
    """
    # open file
    handle = open(file_n, "a")
    # write HTML that handles a paragraph
    handle.write("<p>" + text + "</p>\n")
    # close file
    handle.close()

def header(file_n, text='\n', size=1):
    """
        Creates chosen size header.
    """
    # open file
    handle = open(file_n, 'a')
    # write desired size header to file
    handle.write("<h" + str(size) + ">" + text + '</h' + str(size) + '>')
    # close file
    handle.close()

def image(file_n, text="", ):
    """
        Creates an image given a url or file path.
    """
    # open file
    handle = open(file_n, "a")
    # write HTML that handles a division
    handle.write("<img src='" + text + "'>\n")
    # close file
    handle.close()

def link(file_n, url, text):
    """
        Creates a link.
    """
    # open file
    handle = open(file_n, "a")
    # write HTML that handles a division
    handle.write("<a href=" + url + ">" + text + "</a>\n")
    # close file
    handle.close()

def division(file_n, text):
    """
        Creates a divison, or diferently colered area.
    """
    # open file
    handle = open(file_n, "a")
    # write HTML that handles a division
    handle.write("<div>" + text + "</div>\n")
    # close file
    handle.close()

# create example website
if __name__ == "__main__":
    # open a file
    FILE_NAME = file_name("example.html")
    # clear the file
    clear(FILE_NAME)
    # create the css for the Website
    css(FILE_NAME, background="green", paraback="green", divback="rgb(100,100,200)")
    # add content to the Website
    header(FILE_NAME, "Header 1", 1)
    header(FILE_NAME, "Header 2", 2)
    header(FILE_NAME, "Header 3", 3)
    header(FILE_NAME, "Header 4", 4)
    paragraph(FILE_NAME, "Paragraph")
    division(FILE_NAME, "Division")
    link(FILE_NAME, "https://www.rapidtables.com/web/color/RGB_Color.html", "RGB values")
    paragraph(FILE_NAME, "Image:")
    image(FILE_NAME,
          "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.sketchappsources.com%2F" +
          "resources%2Fsource-image%2Fpython-logo.png&f=1&nofb=1"
         )
