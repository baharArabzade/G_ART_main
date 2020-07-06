from django.urls import path
from Gart import views



urlpatterns = [
    path('', views.HomeView.as_view(), name ='G_Art_Home'),
    path('studio/', views.StudioView.as_view(), name='StudioHome'),
    path('studio/<int:studio_item_id>/', views.Studio_Detail_View.as_view(), name='studio-item-detail'),
    path('tutorial/', views.TutorialView.as_view(), name='TutorialoHome'),
    path('tutorial/<int:tutorial_item_id>/', views.Tutorial_Detail_View.as_view(), name='tutorial-item-detail'),
    path('collection/', views.CollectionView.as_view(), name='CollectionHome'),
    path('collection/<int:collection_item_id>/', views.Collection_Detail_View.as_view(), name='collection-item-detail'),
    path('event/', views.EventView.as_view(), name='EventHome'),
    path('event/<int:event_item_id>/', views.Event_Detail_View.as_view(), name='event-item-detail'),
]
