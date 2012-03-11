(function() {
  var $, GoogleMap, LatLng, LatLngBounds, Map, MapTypeId, Polyline, log, _ref, _ref2;
  var __slice = Array.prototype.slice;

  log = function() {
    var args, _ref;
    args = 1 <= arguments.length ? __slice.call(arguments, 0) : [];
    return (_ref = window.console) != null ? _ref.log.apply(_ref, args) : void 0;
  };

  $ = window.jQuery;

  if (!($ != null)) log('django_maps.googlemap: missing window.jQuery');

  _ref = google.maps, Map = _ref.Map, MapTypeId = _ref.MapTypeId, LatLng = _ref.LatLng, Polyline = _ref.Polyline, LatLngBounds = _ref.LatLngBounds;

  if ((_ref2 = window.django_maps) == null) window.django_maps = {};

  window.django_maps.GoogleMap = GoogleMap = (function() {

    function GoogleMap(selector) {
      var el, options;
      el = $(selector);
      el.width() || el.width(640);
      el.height() || el.height(480);
      options = {
        center: new LatLng(-34.397, 150.644),
        zoom: 3,
        mapTypeId: MapTypeId.ROADMAP
      };
      this.map = new Map(el[0], options);
      this.routes = [];
      this.bounds = new LatLngBounds;
    }

    GoogleMap.prototype.addRoute = function(points, _arg) {
      var color, lat, lng, path, route;
      var _this = this;
      color = _arg.color;
      log('addRoute', points);
      path = (function() {
        var _i, _len, _ref3, _results;
        _results = [];
        for (_i = 0, _len = points.length; _i < _len; _i++) {
          _ref3 = points[_i], lat = _ref3.lat, lng = _ref3.lng;
          _results.push(new LatLng(lat, lng));
        }
        return _results;
      })();
      path.map(function(x) {
        return _this.bounds.extend(x);
      });
      this.routes.push(route = new Polyline({
        map: this.map,
        strokeColor: color || '#3355bb',
        strokeOpacity: 1,
        strokeWeight: 3,
        path: path
      }));
      return this.focusAll();
    };

    GoogleMap.prototype.focusAll = function() {
      return this.map.fitBounds(this.bounds);
    };

    return GoogleMap;

  })();

}).call(this);
