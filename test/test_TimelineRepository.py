import TimelineRepository as timelineRepo

def test_ReadTimeline ():
    login = "Login1"
    posts = timelineRepo.readTimeline(login)
    assert len(posts) == 2
    assert posts[0]['id'] == 4
    assert posts[1]['id'] == 3
    assert posts[0]['text'] == "Texto4"
    assert posts[1]['text'] == "Texto3"
