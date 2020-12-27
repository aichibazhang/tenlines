import html2text as ht

if __name__ == '__main__':
    text_maker = ht.HTML2Text()
    # text_maker.ignore_links = True
    text_maker.bypass_tables = False
    file_path = r'youhua.html'
    htmlfile = open(file_path, 'r', encoding='UTF-8')
    htmlpage = htmlfile.read()
    text = text_maker.handle(htmlpage)
    open("1.md", "w").write(text)
