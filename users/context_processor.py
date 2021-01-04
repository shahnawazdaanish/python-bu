from users.models import FriendRequest
import datetime


def header_processor(request):
    date = datetime.datetime.now()
    friend_requests = None
    friend_request_count = 0
    user = None
    if request.user.is_authenticated:
        objects = FriendRequest.objects
        if objects is not None:
            friend_requests = objects.filter(to_user=request.user)
            friend_request_count = friend_requests.count()

        user = request.user

    return {
        'friend_requests': friend_requests,
        'fr_count': friend_request_count,
        'user': user,
        'date': date
    }

    # return {}
