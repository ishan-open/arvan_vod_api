import os
from mimetypes import guess_type
from base64 import b64encode
from http import HTTPStatus
from vod_api import VodApi


API_KEY = "Your Api Key"
TEST_AUDIO= "audio.mp3"
TEST_VIDEO = "video.mp4"
TEST_AUDIO_TRACK = "audio_track.mp3"
TEST_SUBTITLE = "subtitle.srt"
TEST_WATERMARK = "watermark.jpg"

api = VodApi(API_KEY)


def upload_file(file_path) -> str:
    file_id = None

    with open(file_path, "rb") as file:
        filename = b64encode(file_path.encode())
        filetype = b64encode(guess_type(file_path)[0].encode())
        upload_metadata = f"filename {filename.decode()},filetype {filetype.decode()}"
        file_id = api.file.post_file(
            channel_id,
            os.path.getsize(file_path),
            upload_metadata
        ).created_file_id
        data = file.read(1024*1024)
        offset = 0
        while data:
            x = api.file.patch_file(channel_id, file_id, data, offset)
            offset = int(x.upload_offset)
            data = file.read(1024*1024)

    return file_id


# post

def test_post_chennel():
    res = api.channel.post_channel("testing", "this is test")
    global channel_id
    channel_id = res.data.id

    assert res.status_code == HTTPStatus.CREATED


def test_post_audio():
    global audio_id
    audio_file_id = upload_file(TEST_AUDIO)
    res = api.audio.post_audio(channel_id, "test audio", file_id=audio_file_id)
    audio_id = res.data.id
    assert res.status_code == HTTPStatus.CREATED


def test_post_watermark():
    global watermark_id
    with open(TEST_WATERMARK, "rb") as watermark_file:
        res = api.watermark.post_watermark(
            channel_id, "test watermark", watermark_file
        )

    watermark_id = res.data.id
    assert res.status_code == HTTPStatus.CREATED


def test_post_video():
    global video_id
    video_file_id = upload_file(TEST_VIDEO)
    res = api.video.post_video(
        channel_id, "test video",
        file_id=video_file_id, watermark_id=watermark_id,
    )
    video_id = res.data.id
    assert res.status_code == HTTPStatus.CREATED


def test_post_audio_track():
    global audio_track_id
    with open(TEST_AUDIO_TRACK, "rb") as audio_track_file:
        res = api.audio_track.post_audio_track(
            video_id, "fa", audio_track_file
        )
        audio_track_id = res.data.id
        print(audio_track_id)
    
    assert res.status_code == HTTPStatus.CREATED


def test_post_subtitle():
    global subtitle_id
    with open(TEST_SUBTITLE, "rb") as sub_file:
        res = api.subtitle.post_subtitle(video_id, "fa", sub_file)
        subtitle_id = res.data.id

    assert res.status_code == HTTPStatus.CREATED


# get items

def test_get_channels():
    assert api.channel.get_channels().status_code == HTTPStatus.OK


def test_get_audios():
    assert api.audio.get_audios(channel_id).status_code == HTTPStatus.OK


def test_get_files():
    assert api.file.get_files(channel_id).status_code == HTTPStatus.OK


def test_get_profiles():
    assert api.profile.get_profiles(channel_id).status_code == HTTPStatus.OK


def test_get_subtitles():
    assert api.subtitle.get_subtitles(video_id).status_code == HTTPStatus.OK


def test_get_audio_tracks():
    assert api.audio_track.get_audio_tracks(video_id).status_code == HTTPStatus.OK


def test_get_videos():
    assert api.video.get_videos(channel_id).status_code == HTTPStatus.OK


def test_get_watermarks():
    assert api.watermark.get_watermarks(channel_id).status_code == HTTPStatus.OK

# get

def test_get_channel():
    assert api.channel.get_channel(channel_id).status_code == HTTPStatus.OK


def test_get_video():
    assert api.video.get_video(video_id).status_code == HTTPStatus.OK


def test_get_audio():
    assert api.audio.get_audio(audio_id).status_code == HTTPStatus.OK


def test_get_watermark():
    res = api.watermark.get_watermark(watermark_id)
    assert res.status_code == HTTPStatus.OK


def test_get_audio_track():
    res = api.audio_track.get_audio_track(audio_track_id)
    assert res.status_code == HTTPStatus.OK


def test_get_subtitle():
    assert api.subtitle.get_subtitle(subtitle_id).status_code == HTTPStatus.OK


# patch

def test_patch_video():
    res = api.video.patch_video(video_id, "new title")
    assert res.status_code == HTTPStatus.OK


def test_patch_audio():
    res = api.audio.patch_audio(audio_id, "new title")
    assert res.status_code == HTTPStatus.OK


def test_patch_watermark():
    res = api.watermark.patch_watermark(watermark_id, "new title")
    assert res.status_code == HTTPStatus.OK


def test_patch_channel():
    res = api.channel.patch_channel(channel_id, "new title", "new desc")
    assert res.status_code == HTTPStatus.OK


# delete

def test_delete_watermark():
    res = api.watermark.delete_watermark(watermark_id)
    assert res.status_code == HTTPStatus.OK


def test_delete_audio():
    assert api.audio.delete_audio(audio_id).status_code == HTTPStatus.OK


def test_delete_audio_track():
    res = api.audio_track.delete_audio_track(audio_track_id)
    assert res.status_code == HTTPStatus.OK


def test_delete_subtitle():
    res = api.subtitle.delete_subtitle(subtitle_id)
    assert res.status_code == HTTPStatus.OK


def test_delete_video():
    assert api.video.delete_video(video_id).status_code == HTTPStatus.OK


def test_delete_channel():
    assert api.channel.delete_channel(channel_id).status_code == HTTPStatus.OK
