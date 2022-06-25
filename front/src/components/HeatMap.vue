<template>
  <div id="map-container">
    <svg
      ref="map-svg"
      :width="mapPathsParameters.width"
      :height="mapPathsParameters.height"
      viewBox="0 0 400 400"
    >
      <g class="prefectures"></g>
    </svg>
  </div>
</template>

<script>
import * as d3 from "d3";
import geoJson from "@/assets/japan_geo.json";
export default {
  name: "HeatMap",
  props: {
    populationParameters: {
      type: Object,
      default: () => {},
    },
  },
  data() {
    return {
      mapImage: null,
      mapPathsParameters: {
        width: 400,
        height: 400,
      },
    };
  },
  computed: {},
  mounted() {
    // 地図の投影設定
    const projection = d3
      .geoMercator()
      .center([137.0, 38.2])
      .translate([
        this.mapPathsParameters.width / 2,
        this.mapPathsParameters.height / 2,
      ])
      .scale(1000);
    // 地図をpathに投影(変換)
    const path = d3.geoPath().projection(projection);

    // SVG要素を追加
    this.mapImage = d3
      .select("#map-container svg g")
      .selectAll("path")
      .data(geoJson.features)
      .enter()
      .append("path")
      .attr("d", path)
      .attr("stroke", "#666")
      .attr("stroke-width", 0.25)
      .attr("cursor", "pointer")
      .on("click", (__, item) => this.clickActions(item));

    // ズーム操作系のイベントハンドラを登録
    let zoomHandler = d3.zoom().on("zoom", this.zoomActions);
    zoomHandler(d3.select("#map-container svg"));
  },
  watch: {
    populationParameters: function (newData, oldData) {
      this.repaintMap(newData);
    },
  },

  methods: {
    /**
     * 地図の塗替え
     * @param {object} data 透明度の基準となるデータ
     */
    repaintMap(data) {
      this.mapImage.attr("fill", "#FF0033").attr("fill-opacity", (item) => {
        // 透明度をランダムに指定する (0.0 - 1.0)
        // console.log(data);
        console.log(item.properties.name_ja);
        return data[item.properties.name_ja] || 0.1;
      });
    },
    /**
     * 地図の移動・拡大縮小
     * @param {event}
     */
    zoomActions(event) {
      d3.select("#map-container svg g").attr("transform", event.transform);
    },
    clickActions(item) {
      console.log(item);
      this.$emit("clickedPrefecture", item.properties.name_ja);
    },
  },
};
</script>

<style scoped>
#map-container,
svg {
  width: 100%;
  height: 100%;
}
</style>
