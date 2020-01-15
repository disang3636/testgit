from icrawler.builtin import BaiduImageCrawler, BingImageCrawler
import os
import shutil

def image_crawler(baidu_path, bing_path, number_of_image, image_key_words):
    baidu_storage = {'root_dir': baidu_path}
    bing_storage = {'root_dir': bing_path}


    baidu_crawler = BaiduImageCrawler(parser_threads=8,
                                  downloader_threads=8,
                                  storage=baidu_storage

                                  )

    bingcrawler = BingImageCrawler(parser_threads=8,
                                  downloader_threads=8,
                                  storage=bing_storage

                                   )
    baidu_crawler.crawl(keyword=image_key_words,
                        max_num=number_of_image,min_size=(200,200))
    bingcrawler.crawl(keyword=image_key_words,
                        max_num=number_of_image, min_size=(200,200))

if __name__ == '__main__':
    baidu = 'baidu'
    bing = 'bing'
    names = []
    baidu_path = ''
    bing_path = ''
    for name in open("./to_crawl.txt","r", encoding='utf8'):
        image_key_word = name.strip('\n')
        print("downloading" + image_key_word)
        baidu_path = baidu_path + '/' + image_key_word
        bing_path = bing + '/' + image_key_word
        if(os.path.exists(baidu_path)):
            print("dir" + baidu_path + "already exists, will be removed")
            shutil.rmtree(baidu_path)
            os.mkdir(baidu_path)
        
        if(os.path.exists(bing_path)):
            print("dir" + bing_path + "already exists, will be removed")
            shutil.rmtree(bing_path)
            os.mkdir(bing_path)
        image_crawler(baidu_path, bing_path, number_of_image=400, image_key_words=image_key_word)
        exit()
    # image_key_words = '紫薯布丁'
    # num_of_image = 10
    # image_crawler(baidu_path, bing_path, number_of_image=10, image_key_words=image_key_words)
