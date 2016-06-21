#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
from spyne import Application, srpc, Array, ComplexModel, Integer, String, Boolean, \
    ServiceBase, ResourceNotFoundError, XmlAttribute
from spyne.decorator import srpc, rpc
from spyne.service import ServiceBase
from spyne.model.primitive import Integer
from spyne.model.primitive import AnyUri, DateTime
from spyne.model.enum import Enum
from spyne.model.fault import Fault

import requests

import logging
logger = logging.getLogger('root')
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)


class deleteContainerResult(ComplexModel):
    """SOAP complex type
    ``{http://www.sonos.com/Services/1.1}deleteContainerResult``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    pass


class deviceAuthTokenResult(ComplexModel):
    """SOAP complex type
    ``{http://www.sonos.com/Services/1.1}deviceAuthTokenResult``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    authToken = String
    privateKey = String


class deviceLinkCodeResult(ComplexModel):
    """SOAP complex type
    ``{http://www.sonos.com/Services/1.1}deviceLinkCodeResult``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    regUrl = String
    linkCode = String
    showLinkCode = Boolean
    linkDeviceId = String


class httpHeader(ComplexModel):
    """SOAP complex type ``{http://www.sonos.com/Services/1.1}httpHeader``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    header = String
    value = String


class httpHeaders(ComplexModel):
    """SOAP complex type ``{http://www.sonos.com/Services/1.1}httpHeaders``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    httpHeader = Array(httpHeader)


class mediaRequestInfo(ComplexModel):
    """SOAP complex type ``{http://www.sonos.com/Services/1.1}mediaRequestInfo``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    uri = AnyUri
    httpHeaders = httpHeaders


class addToContainerResult(ComplexModel):
    """SOAP complex type
    ``{http://www.sonos.com/Services/1.1}addToContainerResult``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    updateId = String


class reorderContainerResult(ComplexModel):
    """SOAP complex type
    ``{http://www.sonos.com/Services/1.1}reorderContainerResult``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    updateId = String


class relatedText(ComplexModel):
    """SOAP complex type ``{http://www.sonos.com/Services/1.1}relatedText``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    id = String
    type = String


itemType = Enum('artist',
                'album',
                'genre',
                'playlist',
                'track',
                'search',
                'stream',
                'show',
                'program',
                'favorites',
                'favorite',
                'collection',
                'container',
                'albumList',
                'trackList',
                'streamList',
                'artistTrackList',
                'other',
                type_name="itemType")


class relatedPlay(ComplexModel):
    """SOAP complex type ``{http://www.sonos.com/Services/1.1}relatedPlay``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    id = String
    itemType = itemType
    title = String
    canPlay = Boolean


class streamMetadata(ComplexModel):
    """SOAP complex type ``{http://www.sonos.com/Services/1.1}streamMetadata``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    currentHost = String
    currentShowId = String
    currentShow = String
    secondsRemaining = Integer
    secondsToNextShow = Integer
    bitrate = Integer
    logo = String
    hasOutOfBandMetadata = Boolean
    description = String
    isEphemeral = Boolean
    reliability = AnyUri
    title = AnyUri
    subtitle = AnyUri
    nextShowSeconds = AnyUri


class createContainerResult(ComplexModel):
    """SOAP complex type
    ``{http://www.sonos.com/Services/1.1}createContainerResult``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    id = String
    updateId = String


class relatedBrowse(ComplexModel):
    """SOAP complex type ``{http://www.sonos.com/Services/1.1}relatedBrowse``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    id = String
    type = String


class removeFromContainerResult(ComplexModel):
    """SOAP complex type
    ``{http://www.sonos.com/Services/1.1}removeFromContainerResult``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    updateId = String


class segmentMetadata(ComplexModel):
    """SOAP complex type ``{http://www.sonos.com/Services/1.1}segmentMetadata``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    id = String
    trackId = String
    track = String
    artistId = String
    artist = String
    composerId = String
    composer = String
    albumId = String
    album = String
    albumArtistId = String
    albumArtist = String
    genreId = String
    genre = String
    showId = String
    show = String
    episodeId = String
    episode = String
    host = String
    topic = String
    rating = Integer
    albumArtURI = String
    startTime = DateTime
    duration = Integer


class segmentMetadataList(ComplexModel):
    """SOAP complex type
    ``{http://www.sonos.com/Services/1.1}segmentMetadataList``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    startTime = DateTime
    duration = Integer
    segmentMetadata = Array(segmentMetadata)


class trackMetadata(ComplexModel):
    """SOAP complex type ``{http://www.sonos.com/Services/1.1}trackMetadata``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    artistId = String
    artist = String
    composerId = String
    composer = String
    albumId = String
    album = String
    albumArtistId = String
    albumArtist = String
    genreId = String
    genre = String
    trackNumber = Integer
    duration = Integer
    rating = Integer
    albumArtURI = String
    canPlay = Boolean
    canSkip = Boolean
    canAddToFavorites = Boolean


class itemRating(ComplexModel):
    """SOAP complex type ``{http://www.sonos.com/Services/1.1}itemRating``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    shouldSkip = Boolean
    messageStringId = String


class lastUpdate(ComplexModel):
    """SOAP complex type ``{http://www.sonos.com/Services/1.1}lastUpdate``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    catalog = String
    favorites = String


class property(ComplexModel):
    """SOAP complex type ``{http://www.sonos.com/Services/1.1}property``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    name = String
    value = String


class dynamicData(ComplexModel):
    """SOAP complex type ``{http://www.sonos.com/Services/1.1}dynamicData``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    property = Array(property)


class renameContainerResult(ComplexModel):
    """SOAP complex type
    ``{http://www.sonos.com/Services/1.1}renameContainerResult``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    pass


class reportPlaySecondsResult(ComplexModel):
    """SOAP complex type
    ``{http://www.sonos.com/Services/1.1}reportPlaySecondsResult``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    interval = Integer


algorithm = Enum('AES/CBC/PKCS#7', type_name="algorithm")


class contentKey(ComplexModel):
    """SOAP complex type ``{http://www.sonos.com/Services/1.1}contentKey``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    uri = AnyUri
    algorithm = algorithm
    keySize = Integer
    value = String
    expiration = Integer
    mediaRequestInfo = mediaRequestInfo


class AbstractMedia(ComplexModel):
    """SOAP complex type ``{http://www.sonos.com/Services/1.1}AbstractMedia``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    id = String
    itemType = itemType
    title = String
    language = String
    country = String
    genreId = String
    genre = String
    twitterId = String
    liveNow = Boolean
    onDemand = Boolean


class credentials(ComplexModel):
    __namespace__ = "http://www.sonos.com/Services/1.1"
    deviceId = String
    deviceProvider = String
    sessionId = String


class mediaCollection(ComplexModel):
    """SOAP complex type ``{http://www.sonos.com/Services/1.1}mediaCollection``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    id = String
    itemType = itemType
    title = String
    language = String
    country = String
    genreId = String
    genre = String
    twitterId = String
    liveNow = Boolean
    onDemand = Boolean
    artist = String
    artistId = String
    canScroll = Boolean
    canPlay = Boolean
    canEnumerate = Boolean
    canAddToFavorites = Boolean
    canCache = Boolean
    canSkip = Boolean
    albumArtURI = String
    authRequired = Boolean
    homogeneous = Boolean
    canAddToFavorite = Boolean
    readOnly = XmlAttribute(Boolean)
    userContent = XmlAttribute(Boolean)
    renameable = XmlAttribute(Boolean)
    containsFavorite = Boolean

class mediaMetadata(ComplexModel):
    """SOAP complex type ``{http://www.sonos.com/Services/1.1}mediaMetadata``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    id = String
    itemType = itemType
    title = String
    language = String
    country = String
    genreId = String
    genre = String
    twitterId = String
    liveNow = Boolean
    onDemand = Boolean
    mimeType = String
    trackMetadata = trackMetadata
    streamMetadata = streamMetadata
    dynamic = dynamicData


class mediaList(ComplexModel):
    """SOAP complex type ``{http://www.sonos.com/Services/1.1}mediaList``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    index = Integer
    count = Integer
    total = Integer
    mediaCollection = mediaCollection.customize(min_occurs=0,
                                                max_occurs='unbounded')
    mediaMetadata = mediaMetadata.customize(min_occurs=0,
                                            max_occurs='unbounded')


class extendedMetadata(ComplexModel):
    """SOAP complex type ``{http://www.sonos.com/Services/1.1}extendedMetadata``
    """
    __namespace__ = "http://www.sonos.com/Services/1.1"
    mediaCollection = mediaCollection
    mediaMetadata = mediaMetadata
    relatedBrowse = Array(relatedBrowse)
    relatedText = Array(relatedText)
    relatedPlay = Array(relatedPlay)


class SessionError(Fault):
    __namespace__ = "http://www.sonos.com/Services/1.1"

    def __init__(self, sessionId):
        # TODO: self.transport.http.resp_code = HTTP_401

        Fault.__init__(self,
                       faultcode='Client.SessionIdInvalid',
                       faultstring='No Valid Token for  %r' % sessionId)


class AuthError(Fault):
    __namespace__ = "http://www.sonos.com/Services/1.1"

    def __init__(self, reason, username, device_id):
        # TODO: self.transport.http.resp_code = HTTP_401
        if reason == "badLogin":

            Fault.__init__(
                self,
                faultcode='Client.LoginInvalid',
                faultstring="Username or Password Fail for %r'" % username)
        elif reason == "freeUser":

            details = {'SonosError': "666", }
            Fault.__init__(
                self,
                faultcode='Client.LoginUnsupported',
                faultstring='%r is not a premium account.' % username,
                detail=details)
        elif reason == "unsupportedTerritory":

            Fault.__init__(
                self,
                faultcode="Client.UnsupportedTerritory",
                faultstring='%r is not in a supported territory.' % username)


class UnsupportedAuthError(Fault):
    __namespace__ = "http://www.sonos.com/Services/1.1"

    def __init__(self, username):
        # TODO: self.transport.http.resp_code = HTTP_401

        Fault.__init__(
            self,
            faultcode='Client.LoginUnsupported',
            faultstring='Login Unsupported for non free user  %r' % username)


class Sonos(ServiceBase):
    """SOAP service ``Sonos`` with target namespace
    https://www.sonos.com/Services/1.1.
    """

    __in_header__ = credentials



    @rpc(String, String, Integer, String, _returns=addToContainerResult)
    def addToContainer(ctx, id, parentId, index, updateString):
        """Parameters:

        ``id`` -- id
        ``parentId`` -- id
        ``index`` -- int
        ``updateId`` -- id

        Returns: addToContainerResponse
        """

        return True

    @rpc(String, String, String, String, _returns=createContainerResult)
    def createContainer(ctx, containerType, title, parentId, seedString):
        """Parameters:

        ``containerType`` -- string
        ``title`` -- string
        ``parentId`` -- id
        ``seedId`` -- id

        Returns: createContainerResponse
        """

        return True

    @srpc(String)
    def createItem(favorite):
        """Parameters:

        ``favorite`` -- idg

        Returns: createItemResponse
        """

        return None

    @rpc(String, _returns=deleteContainerResult)
    def deleteContainer(ctx, id):
        """Parameters:

        ``id`` -- id

        Returns: deleteContainerResponse
        """

        return None

    @rpc(String)
    def deleteItem(ctx, favorite):
        """Parameters:

        ``favorite`` -- id

        Returns: deleteItemResponse
        """

        return None

    @srpc(String, AnyUri)
    def getContentKey(id, uri):
        """Parameters:

        ``id`` -- id
        Returns: getContentKeyResponse
        """
        return None

    @srpc(String, String, String)
    def getDeviceAuthToken(householdId, linkCode, linkDeviceString):
        """Parameters:

        ``householdId`` -- id
        ``linkCode`` -- string
        ``linkDeviceId`` -- string (optional)

        Returns: getDeviceAuthTokenResponse
        """
        return None

    @srpc(String)
    def getDeviceLinkCode(householdString):
        """Parameters:

        ``householdId`` -- id

        Returns: getDeviceLinkCodeResponse
        """
        return None

    @rpc(String, _returns=extendedMetadata)
    def getExtendedMetadata(ctx, id):
        """Parameters:

        ``id`` -- id

        Returns: getExtendedMetadataResponse
        """
        logger.debug("Getting Extended Metadata")

        return None

    @srpc(String, String)
    def getExtendedMetadataText(id, type):
        """Parameters:

        ``id`` -- id
        ``type`` -- string

        Returns: getExtendedMetadataTextResponse
        """
        return None

    @rpc(_returns=lastUpdate)
    def getLastUpdate(ctx):
        """Parameters:


        Returns: getLastUpdateResponse
        """
        logger.debug("Getting Last Update")

        import time
        millis = int(round(time.time() * 1000))
        millis = str(millis)[:-6]

        lastUpdateObj = lastUpdate()
        lastUpdateObj.catalog = millis

        return lastUpdateObj

    @rpc(String, _returns=mediaMetadata, _throws=SessionError)
    def getMediaMetadata(ctx, id):
        """Parameters:

        ``id`` -- id

        Returns: getMediaMetadataResponse
        """
        logger.debug("Getting Media Metadata")

        if "PODCAST:" in id:
            podcast_id_obj = id.split(":")
            podcast_id = podcast_id_obj[1]
            podcast_resp = requests.get("http://mobile-backend.libsyn.com/app/items/app_id/handa/destination_id/97431/version/1.20.7/offset/0/size/50").json()


            podcastIndex = next(index for (index, d) in enumerate(podcast_resp) if d["item_id"] == int(podcast_id))

            track_artistid = "ARTIST:HANDA"
            track_artist = "Hamish and Andy"
            #track_albumid = "ALBUM:"+playlist_entry['media']['albumId']
            podcast_album = "Podcasts"
            podcast_title = podcast_resp[podcastIndex]['item_title']

            podcast_albumarturi = "http://i.imgur.com/v1jGtxO.jpg"
            podcast_duration = podcast_resp[podcastIndex]['roles'][0]['duration']
            if podcast_resp[podcastIndex]['premium_state'] == "free":
                podcast_can_play = True
            else:
                podcast_can_play = False

            mediaListItem = mediaMetadata()
            mediaListItem.id = "PODCAST:" + podcast_id
            mediaListItem.title = podcast_title
            mediaListItem.mimeType = "audio/mp3"
            mediaListItem.itemType = "track"
            mediaListItem.trackMetadata = trackMetadata()
            mediaListItem.trackMetadata.artistId = track_artistid
            mediaListItem.trackMetadata.artist = track_artist
            mediaListItem.trackMetadata.album = podcast_album
            mediaListItem.trackMetadata.albumArtURI = podcast_albumarturi
            mediaListItem.trackMetadata.duration = podcast_duration
            mediaListItem.trackMetadata.canPlay = podcast_can_play


        return mediaListItem

    @rpc(String, _returns=String, _throws=SessionError)
    def getMediaURI(ctx, id):
        """Parameters:

        ``id`` -- id

        Returns: getMediaURIResponse
        """
        logger.debug("Getting Media URI")

        if "PODCAST:" in id:

            podcast_id_obj = id.split(":")
            podcast_id = podcast_id_obj[1]
            podcast_resp = requests.get("http://mobile-backend.libsyn.com/app/items/app_id/handa/destination_id/97431/version/1.20.7/offset/0/size/30").json()
            podcastIndex = next(index for (index, d) in enumerate(podcast_resp) if d["item_id"] == int(podcast_id))
            uri = podcast_resp[podcastIndex]['permalink_url']

        return uri

    @rpc(String,
         Integer,
         Integer,
         Boolean,
         _returns=mediaList,
         _throws=SessionError)
    def getMetadata(ctx, id, index, count, recursive):
        """Parameters:

        ``id`` -- id
        ``index`` -- int
        ``count`` -- int
        ``recursive`` -- boolean (optional)
        Returns: getMetadataResponse
        """
        #logging.error(id)
        logger.debug("Getting Metadata")


        if id == "root":

            podcast_resp = requests.get("http://mobile-backend.libsyn.com/app/items/app_id/handa/destination_id/97431/version/1.20.7/offset/0/size/30").json()

            allListItems = []
            amountOfPlaylists = 0
            totalPodcastsReturned = len(podcast_resp)
            i = 0

            for podcast in  podcast_resp:
                podcast_title = podcast['item_title']
                podcast_id = "PODCAST:" + str(podcast['item_id'])
                podcast_image = "http://i.imgur.com/v1jGtxO.jpg"
                podcast_duration = podcast['roles'][0]['duration']
                mediaListItem = mediaMetadata()
                mediaListItem.id = podcast_id
                if podcast['premium_state'] == "free":
                    podcast_can_play = True
                else:
                    podcast_can_play = False
                mediaListItem.title = podcast_title
                mediaListItem.mimeType = "audio/mp3"
                mediaListItem.itemType = "track"
                mediaListItem.trackMetadata = trackMetadata()
                mediaListItem.trackMetadata.artistId = "ARTIST:HANDA"
                mediaListItem.trackMetadata.artist = "Hamish and Andy"
                mediaListItem.trackMetadata.album = "Podcasts"
                mediaListItem.trackMetadata.albumArtURI = podcast_image
                mediaListItem.trackMetadata.duration = podcast_duration
                mediaListItem.trackMetadata.canPlay = podcast_can_play
                allListItems.append(mediaListItem)


            ret_obj = mediaList(index=0,
                                count=len(allListItems),
                                total=totalPodcastsReturned,

                                canPlay=True,
                                mediaMetadata=allListItems,
                                )

        #elif id == "MENU:PODCASTS":





        if "PODCAST:" in id:
            listOfPodcasts = []
            podcast_id_obj = id.split(":")
            podcast_id = podcast_id_obj[1]
            podcast_resp = requests.get("http://mobile-backend.libsyn.com/app/items/app_id/handa/destination_id/97431/version/1.20.7/offset/0/size/30").json()


            podcastIndex = next(index for (index, d) in enumerate(podcast_resp) if d["item_id"] == int(podcast_id))

            track_artistid = "ARTIST:HANDA"
            track_artist = "Hamish and Andy"
            #track_albumid = "ALBUM:"+playlist_entry['media']['albumId']
            podcast_album = "Podcasts"
            podcast_title = podcast_resp[podcastIndex]['item_title']

            podcast_albumarturi = "http://i.imgur.com/v1jGtxO.jpg"
            podcast_duration = podcast_resp[podcastIndex]['roles'][0]['duration']



            if podcast_resp[podcastIndex]['premium_state'] == "free":
                podcast_can_play = True
            else:
                podcast_can_play = False

            mediaListItem = mediaMetadata()
            mediaListItem.id = "PODCAST:" + podcast_id
            mediaListItem.title = podcast_title
            mediaListItem.mimeType = "audio/mp3"
            mediaListItem.itemType = "track"
            mediaListItem.trackMetadata = trackMetadata()
            mediaListItem.trackMetadata.artistId = track_artistid
            mediaListItem.trackMetadata.artist = track_artist
            mediaListItem.trackMetadata.album = podcast_album
            mediaListItem.trackMetadata.albumArtURI = podcast_albumarturi
            mediaListItem.trackMetadata.duration = podcast_duration
            mediaListItem.trackMetadata.canPlay = podcast_can_play
            listOfPodcasts.append(mediaListItem)
            #logging.info(str(mediaListItem))
            ret_obj = mediaList(index=0,
                                count=len(listOfPodcasts),
                                total=len(listOfPodcasts),
                                mediaMetadata=listOfPodcasts)

        return ret_obj

    @rpc(String, _returns=String)
    def getScrollIndices(ctx, id):
        """Parameters:

        ``id`` -- id

        Returns: getScrollIndicesResponse
        """
        logger.debug("Getting Scroll Indices")


        return None


    @rpc(String, String, _returns=String, _throws=AuthError)
    def getSessionId(ctx, username, password):
        """Parameters:

        ``username`` -- string
        ``password`` -- string

        Returns: getSessionIdResponse
        """
        logger.debug("Getting Session ID")

        return None


    @rpc(String, DateTime, Integer, _returns=String, _throws=AuthError)
    def getStreamingMetadata(ctx, id, startTime, duration):
        """Parameters:

        ``id`` -- id
        ``startTime`` -- dateTime
        ``duration`` -- int

        Returns: getStreamingMetadataResponse
        """
        logging.error("GETSTREAMINGMETADATA")

        return "asd"

    @srpc(String, Integer)
    def rateItem(id, rating):
        """Parameters:

        ``id`` -- id
        ``rating`` -- int

        Returns: rateItemResponse
        """
        return None

    @rpc(String, String, String, _returns=removeFromContainerResult)
    def removeFromContainer(ctx, id, indices, updateString):
        """Parameters:

        ``id`` -- id
        ``indices`` -- string
        ``updateId`` -- id

        Returns: removeFromContainerResponse
        """
        logging.info("REMOVE FROM CONTAINER")
        return None

    @rpc(String, String, _returns=renameContainerResult)
    def renameContainer(ctx, id, title):
        """Parameters:

        ``id`` -- id
        ``title`` -- string

        Returns: renameContainerResponse
        """
        logging.info("RENAME CONTAINER")
        return None

    @rpc(String, String, Integer, String)
    def reorderContainer(ctx, id, ffrom, to, updateString):
        """Parameters:

        ``id`` -- id
        ``from`` -- string
        ``to`` -- int
        ``updateId`` -- id

        Returns: reorderContainerResponse
        """
        logger.info("REORDER CONTAINER")
        return None

    @srpc(String)
    def reportAccountAction(type):
        """Parameters:

        ``type`` -- string

        Returns: reportAccountActionResponse
        """
        return None

    @srpc(String, Integer)
    def reportPlaySeconds(id, seconds):
        """Parameters:

        ``id`` -- id
        ``seconds`` -- int

        Returns: reportPlaySecondsResponse
        """
        return None

    @srpc(String, String)
    def reportPlayStatus(id, status):
        """Parameters:

        ``id`` -- id
        ``status`` -- string

        Returns: reportPlayStatusResponse
        """
        return None

    @srpc(String, Integer, String)
    def reportStatus(id, errorCode, message):
        """Parameters:

        ``id`` -- id
        ``errorCode`` -- int
        ``message`` -- string

        Returns: reportStatusResponse
        """
        return None

    @rpc(String,
         String(encoding="utf-8"),
         Integer,
         Integer,
         _returns=mediaList)
    def search(ctx, id, term, index, count):
        """Parameters:

        ``id`` -- id
        ``term`` -- string
        ``index`` -- int
        ``count`` -- int

        Returns: searchResponse
        """
        logger.debug("Getting Search")

        return None

    @rpc(String, Integer)
    def setPlayedSeconds(ctx, id, seconds):
        """Parameters:

        ``id`` -- id
        ``seconds`` -- int

        Returns: setPlayedSecondsResponse
        """
        logger.debug("Setting Played Seconds")



        return None

#Sonos.event_manager.add_listener('method_return_string', Sonos._method_return_string)

WSDL_TYPES = {
    'AbstractMedia': AbstractMedia,
    'addToContainerResult': addToContainerResult,
    'contentKey': contentKey,
    'createContainerResult': createContainerResult,
    'deleteContainerResult': deleteContainerResult,
    'deviceAuthTokenResult': deviceAuthTokenResult,
    'deviceLinkCodeResult': deviceLinkCodeResult,
    'dynamicData': dynamicData,
    'extendedMetadata': extendedMetadata,
    'httpHeader': httpHeader,
    'httpHeaders': httpHeaders,
    'id': id,
    'itemRating': itemRating,
    'lastUpdate': lastUpdate,
    'mediaCollection': mediaCollection,
    'mediaList': mediaList,
    'mediaMetadata': mediaMetadata,
    'mediaRequestInfo': mediaRequestInfo,
    'property': property,
    'relatedBrowse': relatedBrowse,
    'relatedText': relatedText,
    'relatedPlay': relatedPlay,
    'removeFromContainerResult': removeFromContainerResult,
    'renameContainerResult': renameContainerResult,
    'reorderContainerResult': reorderContainerResult,
    'reportPlaySecondsResult': reportPlaySecondsResult,
    'segmentMetadata': segmentMetadata,
    'segmentMetadataList': segmentMetadataList,
    'streamMetadata': streamMetadata,
    'trackMetadata': trackMetadata,
    'algorithm': algorithm,
    'itemType': itemType
}
