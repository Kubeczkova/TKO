from wagtail import hooks
from wagtail.admin.viewsets.pages import PageListingViewSet

from tko.models import ArticlePage
from wagtail.admin.wagtail_hooks import ExplorerMenuItem


class ArticlePageListingViewSet(PageListingViewSet):
    icon = "globe"
    menu_label = "Articles"
    add_to_admin_menu = True
    model = ArticlePage


article_page_listing_viewset = ArticlePageListingViewSet("article_pages")
@hooks.register('register_admin_viewset')
def register_article_page_listing_viewset():
    return article_page_listing_viewset


# @hooks.register('construct_main_menu')
# def hide_snippets_menu_item(request, menu_items):
#     menu_items[:] = [item for item in menu_items if not isinstance(item, ExplorerMenuItem)]
