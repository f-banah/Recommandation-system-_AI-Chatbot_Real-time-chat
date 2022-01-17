
from django.urls import path,include
from django.contrib import admin
from . import  views 
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[

     path('register/',views.register, name='register'),
     
     path('moderator_register/',views.moderator_register.as_view(), name='moderator_register'),
     
     path('admin_register/',views.admin_register.as_view(), name='admin_register'),
     path('candidate_register/',views.candidate_register.as_view(), name='candidate_register'),
     path('projectOwner_register/',views.projectOwner_register.as_view(), name='projectOwner_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
     path('activate/<uidb64>/<token>', views.ActivateAccountView.as_view(), name='activate'), 
     path('adminProj/',views.homeAdmin, name='adminProj'), 
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"), 
        name="password_reset_complete"),
    
    path('offers/', views.offers, name='offers'),
    path('offerview/<str:pk_test>/', views.offerview, name="offerview"),
     path('offerviewC/<int:pk>/', views.offerviewC.as_view(), name="offerviewC"),
     path('offerviewCNonAuth/<int:pk>/', views.offerviewCNonAuth.as_view(), name="offerviewCNonAuth"),
     path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    path('Ownerview/<str:pk_test>/', views.Ownerview, name="Ownerview"),
    path('Candidateview/<str:pk_test>/', views.Candidateview, name="Candidateview"),
 
    path('create_offer/', views.createOffer, name="create_offer"),
    path('create_offerC/<str:pk>/', views.createOfferC, name="create_offerC"),
    path('update_offer/<str:pk>/', views.updateOffer, name="update_offer"),
    path('deactivate_offer/<str:pk>/', views.deactivateOffer, name="deactivate_offer"),
    path('deactivate_offerA/<str:pk>/', views.deactivateOffera, name="deactivate_offera"),
    path('close_offerA/<str:pk>/', views.closeOffera, name="close_offera"),
    path('close_offer/<str:pk>/', views.closeOffer, name="close_offer"),   
    
    path('offersC/', views.offersC, name='offersC'),  
    path('offersCNON/', views.offersCNON, name='offersCNON'),
    path('offersCandidate/<str:pk>/', views.offersCandidate, name='offersCandidate'),
    path('archivePostulate/', views.archivePostulate, name='archivePostulate'), 
    path('offersCandidateAdmin/<str:pk>/', views.offersCandidateAdmin, name='offersCandidateAdmin'),
    
    path('delete/<str:pk>/', views.delete, name="delete"),
    path('accepter/<str:pk>/<str:vk>', views.accepter, name="accepter"),
    path('Reject/<str:pk>/<str:vk>', views.Reject, name="Reject"),
    
    path('team/<str:pk>/', views.team, name='team'),
    path('Candidateteam/<str:pk>/', views.Candidateteam, name="Candidateteam"),
    path('CandidateteamAdmin/<str:pk>/', views.CandidateteamAdmin, name="CandidateteamAdmin"),
    
    
    
    
    
    path('indexC/', views.indexC, name="indexC"),
    path('indexP/', views.indexP, name="indexP"),
    path('indexO/', views.indexO, name="indexO"),
    path('indexT/', views.indexT, name="indexT"),
    path('deactivateTeam/<str:pk>/', views.deactivateTeam, name="deactivateTeam"),
    path('deactivateUser/<str:pk>/', views.deactivateUser, name="deactivateUser"),
    path('deactivateAccount/<str:pk>/', views.deactivateAccount, name="deactivateAccount"),
    path('OfferOwner/<str:pk>/', views.OfferOwner, name="OfferOwner"),
    path('OfferPosul/<str:pk>/', views.OfferPosul, name="OfferPosul"),
    path('teamsC/<str:pk>/', views.teamsC, name="teamsC"),
    path('teamOwner/<str:pk>/', views.teamOwner, name="teamOwner"),
    
    path('indexCC/', views.indexCC, name="indexCC"),
    path('indexPP/', views.indexPP, name="indexPP"),
    path('indexOO/', views.indexOO, name="indexOO"),
    path('indexTT/', views.indexTT, name="indexTT"),
    path('OfferOwnerR/<str:pk>/', views.OfferOwnerR, name="OfferOwnerR"),
    path('OfferPosulL/<str:pk>/', views.OfferPosulL, name="OfferPosulL"),
    path('teamsCC/<str:pk>/', views.teamsCC, name="teamsCC"),
    path('teamOwnerR/<str:pk>/', views.teamOwnerR, name="teamOwnerR"),
    path('moderators/', views.moderators, name="moderators"),
    
    path('teamsCandidate/', views.teamsCandidate, name="teamsCandidate"),
    path('teamsOwner/', views.teamsOwner, name="teamsOwner"),
    
    
    path('recommend/', views.recommend, name='recommend'),
    path('notifications',views.notifications, name='notifications'),
    path('roomUser',views.roomUser, name='roomUser'),
    path('<str:room>/', views.room, name='room'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    
    path('checkview', views.checkview, name='checkview'),
    
    path('roomAdminOwner',views.roomAdminOwner, name='roomAdminOwner'),
    path('roomOwnerAdmin',views.roomOwnerAdmin, name='roomOwnerAdmin'),
    path('checkviewAdmin', views.checkviewAdmin, name='checkviewAdmin'),
     path('sendAdmin', views.sendAdmin, name='sendAdmin'),
     path('getMessagesAdmin/<str:room>/', views.getMessagesAdmin, name='getMessagesAdmin'),
     path('chat/<str:room>/', views.roomAdmin, name='roomAdmin'),
     path('allrooms', views.allrooms, name='allrooms'),
     path('teamOffer/<str:pk>/', views.teamOffer, name='teamOffer'),
     path('roomOffer/<str:pk>/', views.roomOffer, name='roomOffer'),
     
     path(r'download/<int:file_pk>',views.download,name="download"),
    path('deactivateRoom/<str:pk>/', views.deactivateRoom, name="deactivateRoom"), 
     
    
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#when adding urls.py to main change the "from main import views" to "from . import views"
