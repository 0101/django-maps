log = (args...) -> window.console?.log args...

$ = window.jQuery
if not $?
  log 'django_maps.googlemap: missing window.jQuery'


{Map, MapTypeId, LatLng, Polyline, LatLngBounds} = google.maps


window.django_maps ?= {}
window.django_maps.GoogleMap = class GoogleMap

  constructor: (selector) ->

    el = $(selector)
    el.width() or el.width 640
    el.height() or el.height 480

    options =
      center: new LatLng -34.397, 150.644
      zoom: 3
      mapTypeId: MapTypeId.ROADMAP

    @map = new Map el[0], options
    @routes = []

    @bounds = new LatLngBounds

  addRoute: (points, {color}) ->
    log 'addRoute', points

    path = (new LatLng(lat, lng) for {lat, lng} in points)

    path.map (x) => @bounds.extend x

    @routes.push route = new Polyline
      map: @map
      strokeColor: color or '#3355bb'
      strokeOpacity: 1
      strokeWeight: 3
      path: path

    @focusAll()

  focusAll: -> @map.fitBounds @bounds





