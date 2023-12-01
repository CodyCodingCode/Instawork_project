from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import TeamMember
from .forms import TeamMemberForm


class TeamMemberListView(ListView):
    model = TeamMember
    template_name = 'members/team_member_list.html'
    context_object_name = "team_members"


class TeamMemberCreateView(CreateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'members/team_member_form.html'
    success_url = reverse_lazy('member_list')


class TeamMemberUpdateView(UpdateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'members/team_member_edit.html'
    success_url = reverse_lazy('member_list')


class TeamMemberDeleteView(DeleteView):
    model = TeamMember
    success_url = reverse_lazy('team_member_list')

