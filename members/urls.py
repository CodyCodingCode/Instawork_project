
from django.urls import path
from .views import TeamMemberListView, TeamMemberCreateView, TeamMemberUpdateView, TeamMemberDeleteView

urlpatterns = [
    path('members/list/', TeamMemberListView.as_view(), name='team_member_list'),
    path('members/create/', TeamMemberCreateView.as_view(), name='team_member_create'),
    path('', TeamMemberListView.as_view(), name='member_list'),
    path('<int:pk>/', TeamMemberUpdateView.as_view(), name='team_member_edit'),
    path('<int:pk>/delete/', TeamMemberDeleteView.as_view(), name='team_member_delete'),
]
