      // Initializing the map
      var map = L.map('map').setView([23.6978, 120.9605], 7)
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap'
      }).addTo(map);


      // Geolocation
      map.locate({setView: true, maxZoom: 16});
        // handle LocationFound
      function onLocationFound(e) {
        let radius = e.accuracy;
        
        L.marker(e.latlng).addTo(map)
          .bindPopup(`您在這附近 (方圓${radius}公尺內)`).openPopup();
        L.circle(e.latlng, radius).addTo(map);
      }
      map.on('locationfound', onLocationFound);
        // handle LocationError
      function onLocationError(e) {
        alert(e.message);
      }
      map.on('locationerror', onLocationError);


      // read main DF
      const url = 'https://nricm101-map.chienhsiang-hung.eu.org/api/get';
      fetch(`${url}`)
      .then(response => {
        return response.json();
      })
      .then(jsondata => {
        let free_layer = L.layerGroup([]),
            notfree_layer = L.layerGroup([]);

        for (let key in jsondata) {
          
          let notes = jsondata[key]["('就診中醫院所前請先點選西醫快篩陽性判斷視訊院所', '下方為中醫院所LINE ID')"]

          let my_marker = L.marker(jsondata[key]["('LatLon', 'LatLon')"])
            .bindPopup(
              `<p>
                ${jsondata[key]["('全聯會提供公費清冠一號民眾意見反應專區', '醫療院所名稱')"]} <br>
                  清冠剩餘人次 ${jsondata[key]["('剩餘人次', '剩餘人次')"]} <br>
                  公費 ${jsondata[key]["('原廠清冠一號照片', '清冠一號公費')"] == '是' ? '是':'否'} <br>
                  ${jsondata[key]["(nan, '電話')"]} <br>
                  ${jsondata[key]["(nan, '地址')"]} <br>
                  <hr>
                  備註 ${JSON.stringify(notes) == '{"$numberDouble":"NaN"}' ? '' : notes}
              </p>`
            )
            .addTo(jsondata[key]["('原廠清冠一號照片', '清冠一號公費')"] == '是'? free_layer:notfree_layer);
          
           //my_marker._icon.classList.add(jsondata[key]["('剩餘人次', '剩餘人次')"]*1 > 0 ? "success" : "fail");
           my_marker.on('mouseover', function() {
            my_marker.openPopup();
           });
           my_marker.on('click', function() {
            my_marker.openPopup();
           });
        };
      })
      .then(() => {
        layerControl.addOverlay(free_layer, "公費");
        layerControl.addOverlay(notfree_layer, "非公費")
        $('.center-screen').css('display', 'none');
      });

      /*
      L.popup()
        .setLatLng([24.137785, 120.612262])
        .setContent("I am a standalone popup.")
        .openOn(map);      
      */