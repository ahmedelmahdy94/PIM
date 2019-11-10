from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Pagination ():
    def do_paginate(data_list, page_number):
        ret_data_list = data_list
        # number of records in each page.
        result_per_page = 5
        paginator = Paginator(data_list, result_per_page)
        try:
            # get data list for the specified page_number.
            ret_data_list = paginator.page(page_number)
        except EmptyPage:
            # get the lat page data if the page_number is bigger than last page number.
            ret_data_list = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            # if the page_number is not an integer then return the first page data.
            ret_data_list = paginator.page(1)
        return [ret_data_list, paginator]
