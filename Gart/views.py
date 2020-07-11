from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render

from .models import Studio_item, Tutorial_item, Collection_item, Event_item, Studio_Photo


class HomeView(TemplateView):
    template_name = "HomePage.html"


class StudioView(TemplateView):
    template_name = "studio/studioHome.html"

    def get(self, request, *args, **kwargs):
        studio_items = Studio_item.objects.all()
        self.extra_context = {
            'studio_items': studio_items,
        }
        return self.render_to_response(self.get_context_data())


class Studio_Detail_View(TemplateView):

    def get(self, request, *args, **kwargs):

        studio_item_id = kwargs.get('studio_item_id')
        studio_item = get_object_or_404(Studio_item, pk=studio_item_id)
        studio_photo_list = Studio_Photo.objects.all().filter(studio_item=studio_item_id)
        crew = []
        myCrew = []
        myInfoTable = []
        infotable = []
        nomination = []
        award = []
        myNomination = []
        myAward = []

        if (studio_item.info_table):
            infotable = studio_item.info_table.split("\r\n")
        if (studio_item.nomination):
            nomination = studio_item.nomination.split("\r\n")
        if (studio_item.award):
            award = studio_item.award.split("\r\n")
        if (studio_item.crew):
            crew = studio_item.crew.split("\r\n")

        for i in range(0, len(infotable)):
            str1 = infotable[i].split("=")
            myInfoTable.append([str1[0], str1[1]])
        for i in range(0, len(nomination)):
            str2 = nomination[i].split("link=")
            myNomination.append([str2[0], str2[1]])
        for i in range(0, len(award)):
            str3 = award[i].split("link=")
            myAward.append([str3[0], str3[1]])
        for i in range(0, len(crew)):
            str4 = crew[i].split("=")
            myCrew.append([str4[0], str4[1]])

        movie=0;
        music_video=0;
        if (studio_item.type=="movie"):
            movie=1
        if(studio_item.type=="music video"):
            music_video=1
        self.extra_context = {

            'studio_item_id': studio_item_id,
            'studio_item': studio_item,
            'myInfoTable': myInfoTable,
            'myNomination': myNomination,
            'myAward': myAward,
            'myCrew': myCrew,
            'studio_photo_list':studio_photo_list,
            'movie':movie,
            'music_video':music_video,
        }

        return render(request, 'studio/detail.html', self.get_context_data())


class TutorialView(TemplateView):
    template_name = "tutorial/tutorialHome.html"

    def get(self, request, *args, **kwargs):
        tutorial_items = Tutorial_item.objects.all()
        self.extra_context = {
            'tutorial_items': tutorial_items,
        }
        return self.render_to_response(self.get_context_data())


class Tutorial_Detail_View(TemplateView):

    def get(self, request, *args, **kwargs):
        tutorial_item_id = kwargs.get('tutorial_item_id')
        tutorial_item = get_object_or_404(Tutorial_item, pk=tutorial_item_id)

        self.extra_context = {
            'tutorial_item_id': tutorial_item_id,
            'tutorial_item': tutorial_item,

        }

        return render(request, 'tutorial/tutorialDetail.html', self.get_context_data())


class CollectionView(TemplateView):
    template_name = "collection/collectionHome.html"

    def get(self, request, *args, **kwargs):
        collection_items = Collection_item.objects.all()
        self.extra_context = {
            'collection_items': collection_items,
        }
        return self.render_to_response(self.get_context_data())


class Collection_Detail_View(TemplateView):

    def get(self, request, *args, **kwargs):

        collection_item_id = kwargs.get('collection_item_id')
        collection_item = get_object_or_404(Collection_item, pk=collection_item_id)
        if (collection_item.poster):
            a = 1
        else:
            a = 0
        self.extra_context = {
            'collection_item_id': collection_item_id,
            'collection_item': collection_item,
            'a': a,

        }

        return render(request, 'collection/collectionDetail.html', self.get_context_data())


class EventView(TemplateView):
    template_name = "event/eventHome.html"

    def get(self, request, *args, **kwargs):
        event_items = Event_item.objects.all()
        self.extra_context = {
            'event_items': event_items,
        }
        return self.render_to_response(self.get_context_data())


class Event_Detail_View(TemplateView):

    def get(self, request, *args, **kwargs):
        event_item_id = kwargs.get('event_item_id')
        event_item = get_object_or_404(Event_item, pk=event_item_id)
        self.extra_context = {
            'event_item_id': event_item_id,
            'event_item': event_item,

        }

        return render(request, 'event/eventDetail.html', self.get_context_data())
