<template>
  <div class="home">
    <transition name="fade" mode="out-in">

      <dv-border-box-10>
        <div class="naca">
          <div class="index-header" style="margin-top: 5px">
            <div>
              <dv-decoration-10 style="width: 450px; height: 1px; margin-bottom: 45px" />
              <dv-decoration-8 style="width: 180px; height: 50px" :color="['#568aea', '#000000']" />
              <div style="
                  width: 150px;
                  color: #eeecec;
                  font-size: 18px;
                  padding: 0 15px;
                  font-weight: bold;
                ">
                数据中心
              </div>
              <dv-decoration-8 :reverse="true" style="width: 180px; height: 50px" :color="['#568aea', '#000000']" />
              <dv-decoration-10 style="
                  width: 450px;
                  height: 1px;
                  transform: rotateY(180deg);
                  margin-bottom: 45px;
                " />
            </div>
            <dv-decoration-5 style="width: 10%; height: 20px" :color="['#568aea', '#000000']" />
          </div>

          <div class="index-content">
            <div class="left">
              <div class="col-1" style="width: 600px">

                <dv-border-box-12>
                  <div style="padding: 5px">
                    <div class="title" style="margin-top: 5px">
                      各种鱼群的数量
                    </div>

                    <div ref="firstMain" style="width: 100%; height: 120px"></div>
                  </div>
                </dv-border-box-12>
                <dv-border-box-12>
                  <div style="padding: 5px;padding-bottom:30px">
                    <div class="title" style="margin-top: 1px">水质数据</div>
                    <dv-scroll-board ref="scrollBoard" :config="config1" style="width: 100%; height: 110px" />
                  </div>
                </dv-border-box-12>


                <dv-border-box-8>
                  <div style="padding: 15px">
                    <div class="title" style="margin-top: 5px">传感器信息</div>
                    <!-- <div ref="timeZhou" style="width: 100%; height: 350px"></div> -->
                    <dv-scroll-board :config="config2" style="width: 100%; height: 110px" />
                  </div>
                </dv-border-box-8>



              </div>
            </div>

            <div class="cent">
              <div class="col-2" style="height: 100%; width: 100%">

                <dv-border-box-12 style="height: 100%; width: 100%">
                  <div class="title" style="margin-top: 5px">
                    当日天气
                  </div>
                  <!-- <div ref="fourthMain" style="width: 93%; height: 83%; margin-left: 15px"> -->
                  <div ref="secondMain" style="width: 100%; height: 100%"></div>
                  <!-- </div> -->
                </dv-border-box-12>

              </div>
            </div>

            <div class="right">
              <div class="col-3" style="">
                <dv-border-box-12>
                  <div style="padding: 15px">
                    <div class="title" style="margin-top: 5px">
                      访问次数统计
                    </div>
                    <dv-capsule-chart :config="config3" style="width:300px;height:40px" />

                    <div id="secondMian" style="width: 100%; height: 110px"></div>
                  </div>
                </dv-border-box-12>

                <dv-border-box-12>
                  <div style="padding: 1px">
                    <div class="title" style="margin-top: 5px">
                      气温曲线
                    </div>
                    <div ref="thirdMain" style="width: 400px; height: 200px"></div>
                  </div>
                </dv-border-box-12>

<dv-border-box-9 :color="['#568aea']">
  <div style="padding: 20px; color: white;">
    <div class="title" style="margin-top: 5px; color: white;">
      天气预报
    </div>
    <div style="height: 90%; margin-top: 10px;">
      <div>明天: {{ weather_data.forecasts[0].casts[1].dayweather }} {{ weather_data.forecasts[0].casts[1].daytemp }}°C/{{ weather_data.forecasts[0].casts[1].nighttemp }}°C  {{ weather_data.forecasts[0].casts[1].daywind }}风  风力{{ weather_data.forecasts[0].casts[1].daypower }}级</div>
      <div>后天: {{ weather_data.forecasts[0].casts[2].dayweather }} {{ weather_data.forecasts[0].casts[2].daytemp }}°C/{{ weather_data.forecasts[0].casts[2].nighttemp }}°C  {{ weather_data.forecasts[0].casts[2].daywind }}风  风力{{ weather_data.forecasts[0].casts[2].daypower }}级</div>
      <div>大后天: {{ weather_data.forecasts[0].casts[3].dayweather }} {{ weather_data.forecasts[0].casts[3].daytemp }}°C/{{ weather_data.forecasts[0].casts[3].nighttemp }}°C  {{ weather_data.forecasts[0].casts[3].daywind }}风  风力{{ weather_data.forecasts[0].casts[3].daypower }}级</div>
    </div>
  </div>
</dv-border-box-9>
              </div>
            </div>

          </div>
        </div>
      </dv-border-box-10>
    </transition>
  </div>
</template>


<script>
import $ from "jquery";
import LeftTop from "@/components/LeftTop.vue";
import zhanjiang from "@/json/zhanjiang.json";

function formatter(number) {
  const numbers = number.toString().split("").reverse();
  const segs = [];

  while (numbers.length) segs.push(numbers.splice(0, 3).join(""));

  return segs.join(",").split("").reverse().join("");
}
export default {
  name: "Index",
  data() {
    return {
      config1: {
        header: ['时间', 'PH', '溶氧(mg/L)', '温度(°C)', '总氮(mg/L)'],
        data: []
      },
      config2: {
        header: ['设备', '编号', '类型', '大小'],
        data: [
          ['水底摄像头', 'video-1', 'H.264', '4Mb'],
          ['水底摄像头', 'video-2', '4CIF', '128kb'],
          ['水面摄像头', 'video-3', 'H.264', '100b'],
          ['云台', 'holder-1', 'H.264', '1kb'],
          ['声纳', 'sonar-1', 'H.264', '1kb'],
        ]
      },
      config3: {
        data: [
          {
            name: '星期一',
            value: 167
          },
          {
            name: '星期二',
            value: 67
          },
          {
            name: '星期三',
            value: 123
          },
          {
            name: '星期四',
            value: 55
          },
          {
            name: '星期五',
            value: 98
          },
          {
            name: '星期六',
            value: 167
          },
          {
            name: '星期日',
            value: 167
          }
        ],
        showValue: true
      },
      config4: {
        data: [
          {
            name: '北京',
            value: 55
          },
          {
            name: '上海',
            value: 120
          },
          {
            name: '海南',
            value: 78
          },
          {
            name: '厦门',
            value: 66
          },
          {
            name: '深圳',
            value: 80
          },
          {
            name: '贵阳',
            value: 45
          },

        ]
      },
      species_count: [],
      weather_data: [],
      zone_weather: [
        {name: '赤坎区', value: '111'},
        {name: '霞山区', value: '111'},
        {name: '坡头区', value: '111'},
        {name: '麻章区', value: '111'},
        {name: '遂溪县', value: '111'},
        {name: '徐闻县', value: '111'},
        {name: '廉江市', value: '111'},
        {name: '雷州市', value: '111'},
        {name: '吴川市', value: '111'}
      ]
    }
  },
  methods: {
    setMap() {
      // 初始化统计图对象
      var chartDom = this.$refs.secondMain;
      var myChart = this.$echarts.init(chartDom);
      this.$echarts.registerMap("zhanjiang", zhanjiang);
      var option = {
        tooltip: {
          trigger: 'item',
          formatter: function(params) {
            return params.name + ': ' + params.data.value.weather + '<br>'
            + '实时气温: ' + params.data.value.temperature + '°C' + '<br>'
            + '风向: ' + params.data.value.winddirection + '<br>'
            + '风力: ' + params.data.value.windpower + '级' + '<br>'
            + '空气湿度: ' + params.data.value.humidity;
          }
        },
        series: [
          {
            name: '湛江市地图',
            type: 'map',
            map: 'zhanjiang',// 这个是上面注册时的名字哦，registerMap（'这个名字保持一致'）
            label: {
              show: true
            },
            data: this.zone_weather
          }
        ]
      };
      myChart.setOption(option);
    },
    processWeatherData() {
      var forecasts = this.weather_data.forecasts[0].casts;
      var chartDom = this.$refs.thirdMain;
      var myChart = this.$echarts.init(chartDom);

      var option = {
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
            label: {
              backgroundColor: '#6a7985'
            }
          }
        },
        legend: {
          // data: ['Email', 'Union Ads', 'Video Ads', 'Direct', 'Search Engine'],
          textStyle: {
            color: 'white'
          }
        },
        grid: {
          top: '10%',
          left: '3%',
          right: '6%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          axisLabel: {
            color: 'white',
          },
          data: [
            forecasts[0].date.slice(5), 
            forecasts[1].date.slice(5), 
            forecasts[2].date.slice(5), 
            forecasts[3].date.slice(5)
          ]
        },
        yAxis: {
          type: 'value',
          axisLabel: {
            formatter: '{value} °C',
            color: 'white'
          },
          min: 0,
          max: 40,
        },
        series: [
          {
            name: '最高气温',
            type: 'line',
            data: [forecasts[0].daytemp, forecasts[1].daytemp, forecasts[2].daytemp, forecasts[3].daytemp],
            smooth: true
          },
          {
            name: '最低气温',
            type: 'line',
            data: [forecasts[0].nighttemp, forecasts[1].nighttemp, forecasts[2].nighttemp, forecasts[3].nighttemp],
            smooth: true
          }
        ]
      };

      option && myChart.setOption(option);
    },
    setpieData() {
      $(document).ready(() => {
        var chartDom = this.$refs.firstMain;
        var myChart = this.$echarts.init(chartDom);
        var option;
        var option = {
          tooltip: {
            trigger: 'item',
            formatter: "{a}<br/>{b}: {c}({d}%)"
          },
          toolbox: {
            show: true
          },
          calulable: true,

          legend: {
            orient: 'vertical',
            left: 'left',
            top: 'center',
            // data: ['大黄鱼', '鲈鱼', '石斑鱼', '鲷鱼', '军曹鱼'],
            textStyle: {
              color: 'white'
            }
          },
          series: [
            {
              name: '数量',
              type: 'pie',
              radius: ['40%', '70%'],
              avoidLabelOverlap: false,
              label: {
                show: false,
                position: 'center'
              },
              emphasis: {
                label: {
                  show: true,
                  fontSize: 15,
                  fontWeight: 'bold'
                }
              },
              labelLine: {
                show: false
              },
              data: this.species_count
            }
          ]
        };

        option && myChart.setOption(option);
      });
    },
  },
  async created() {
    // 获取全市数据
    const response1 = await axios.get('/weather/weatherInfo', {
      params: {
        key: '0c0f5c504d6a32f8b851a8b9eb2e4247',
        city: '440800',
        extensions: 'all'
      }
    });
    this.weather_data = response1.data;
    // 获取各区数据
    var zone_id = ['440802', '440803', '440804', '440811', '440823', '440825', '440881', '440882', '440883'];
    for (var i = 0; i < zone_id.length; i++) {
      const response2 = await axios.get('/weather/weatherInfo', {
        params: {
          key: '0c0f5c504d6a32f8b851a8b9eb2e4247',
          city: zone_id[i],
          extensions: 'base'
        }
      });
      this.zone_weather[i].value = response2.data.lives[0];
      console.log(this.zone_weather[i].value);
    }
    console.log(this.weather_data);
    const response = await axios.get(`/api/myApp/dataCenter/`);
    this.config1.data = response.data.hydro_data;
    // console.log(this.config1.data);
    this.species_count = response.data.species_stats.species_count;
    // console.log(this.species_count);
    this.$refs['scrollBoard'].updateRows(this.config1.data)
    $(document).ready(async () => {
      this.processWeatherData();
      this.setpieData();
      this.setMap();
      // this.setLastData();
    })
  },
  components: {
    LeftTop,
  },
};
</script>

<style lang="less" scoped>
.loading {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.cent-1-content {
  padding: 20px;
  display: flex;
}

.right-content {
  margin-left: 30px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}

.right-content div {
  display: flex;
  font-size: 15px;
  align-items: center;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}

.cents {
  display: flex;
  flex-direction: column;
}

.above {
  display: flex;
}

.aboveOne {
  display: flex;
  flex-direction: column;
}

.aboveTwo {
  display: flex;
  flex-direction: column;
}

.cent {
  width: 1000px;
  height: 600px;
}

.cent-1 {
  margin: 10px;
  color: aliceblue;
  width: 500px;
  height: 220px;
  /* background-color: rgb(26, 26, 133); */
}

.left {
  display: flex;
  flex-direction: column;
}

.left-1 {
  margin: 15px;
  color: aliceblue;
  width: 550px;
  display: flex;
  flex-direction: column;
}

.left-2 {
  margin: 15px;
  color: aliceblue;
  width: 530px;
  display: flex;
  flex-direction: column;
}

.naca {
  // padding: 35px 15px 0 15px;
  box-sizing: border-box;
  width: 100%;
  // height: 40rem;
  display: flex;
  flex-direction: column;
}

.naca .index-header {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.naca .index-header div {
  display: flex;
  justify-content: center;
  align-items: center;
}

.naca .index-content {
  display: flex;
  justify-content: center;
  align-items: center;
}

.bg {
  width: 100%;
  height: 45rem;
  background-color: black;
  position: relative;
}

.title {
  color: #3f96a5;
  font-size: 18px;
  margin-top: -20px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-weight: bold;
}

.content {
  display: flex;
  align-items: center;
}

.content-word {
  width: 140px;
  height: 130px;
  background: #11193e;
  border-radius: 40px;
  border: 1px solid #3d3d3d;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.content-word-item {
  margin-left: 19px;
  margin-bottom: 10px;

  img {
    width: 20px;
    height: 20px;
  }
}

.content-word-item-title {
  font-size: 18px;
}

.content-word-item-content {
  margin-top: 5px;

  display: flex;
  align-items: center;
}

.row_list {
  list-style: none;
}

.cases_list::-webkit-scrollbar {
  display: none;
}

.cases_list li {
  display: grid;
  -ms-grid-columns: 30px 110px 60px 60px 60px;
  grid-template-columns: 30px 110px 60px 60px 60px;
  cursor: pointer;
  margin-left: 23px;
  text-align: center;
  line-height: 30px;
  color: rgb(238, 236, 236);
}

.list_time {
  height: 30px;
  overflow: auto;
}

.list_time::-webkit-scrollbar {
  display: none;
}
</style>
