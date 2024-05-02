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
                可视化化平台
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
              <div class="col-1" style="">

                <dv-border-box-12 style="height: 300px; width: 490px">
                  <div class="title" style="margin-top: 5px">
                    历史记录
                  </div>
                  <div ref="firstMain" style="width: 100%; height: 105%"></div>
                </dv-border-box-12>

                <dv-border-box-12 style="height: 250px; width: 490px">
                  <div class="title" style="margin-top: 5px">
                    设备状态
                  </div>
                  <div ref="secondMain" style="width: 100%; height: 90px"></div>
                </dv-border-box-12>



              </div>
            </div>

            <div class="cent">
              <div class="col-2" style="">

                <dv-border-box-12 style="height: 300px; width: 410px">
                  <div class="title" style="margin-top: 5px">
                    水文气象
                  </div>
                  <div ref="thirdMain" style="width: 100%; height: 90px"></div>
                </dv-border-box-12>

                <dv-border-box-12 style="height: 250px; width: 410px">
                  <div class="title" style="margin-top: 5px">
                    定位
                  </div>
                  <div ref="fourthMain" style="width: 100%; height: 90px"></div>
                </dv-border-box-12>

              </div>
            </div>

            <div class="right">
              <div class="col-3" style="">
                <dv-border-box-12 style="height: 330px; width: 540px">
                  <div class="title" style="margin-top: 5px">
                    监控视频
                  </div>
                  <div id="fifthMain" style="width: 500px; height: 90px"></div>
                </dv-border-box-12>

                <dv-border-box-12 style="height: 220px; width: 540px">
                  <div class="title" style="margin-top: 5px">
                    附加功能
                  </div>
                  <div id="sixthMain" style="width: 100%; height: 90px"></div>
                </dv-border-box-12>
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
import { color } from "echarts";
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

    };
  },
  methods: {
    setBarData() {
      $(document).ready(() => {
        var chartDom = this.$refs.firstMain;
        var myChart = this.$echarts.init(chartDom);
        var option;
        option = {
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'cross',
              crossStyle: {
                color: '#999'
              }
            }
          },
          toolbox: {
            feature: {
              dataView: { show: false, readOnly: false },
              magicType: { show: true, type: ['line', 'bar'] },
              restore: { show: false },
              saveAsImage: { show: false }
            }
          },
          legend: {
            data: ['Evaporation', 'Precipitation', 'Temperature'],
            textStyle:{
              color: '#ffffff',
            }
          },
          xAxis: [
            {
              type: 'category',
              data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
              axisPointer: {
                type: 'shadow'
              },
              show:false
            }
          ],
          yAxis: [
            {
              type: 'value',
              name: 'Precipitation',
              nameTextStyle: {
                color: '#ffffff',
              },
              min: 0,
              max: 250,
              interval: 50,
              axisLabel: {
                formatter: '{value} ml',
                color: '#ffffff',
                fontSize:10
              }
            },
            {
              type: 'value',
              name: 'Temperature',
              nameTextStyle: {
                color: '#ffffff'
              },
              min: 0,
              max: 25,
              interval: 5,
              axisLabel: {
                formatter: '{value} °C',
                color: '#ffffff',
                fontSize:10
              }
            }
          ],
          series: [
            {
              name: 'Evaporation',
              type: 'bar',
              tooltip: {
                valueFormatter: function (value) {
                  return value + ' ml';
                }
              },
              data: [
                2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3
              ]
            },
            {
              name: 'Precipitation',
              type: 'bar',
              tooltip: {
                valueFormatter: function (value) {
                  return value + ' ml';
                }
              },
              data: [
                2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3
              ]
            },
            {
              name: 'Temperature',
              type: 'line',
              yAxisIndex: 1,
              tooltip: {
                valueFormatter: function (value) {
                  return value + ' °C';
                }
              },
              data: [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]
            }
          ]
        };

        option && myChart.setOption(option);
      });
    },
  },
  async created() {
    $(document).ready(async () => {
      this.setBarData()
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

// .cents {
//   display: flex;
//   flex-direction: column;
// }

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

// .cent {
//   width: 850px;
//   height: 300px;
// }

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

.cent {
  display: flex;
  flex-direction: column;
}

.right {
  display: flex;
  flex-direction: column;
}

.left-1 {
  margin: 5px;
  color: aliceblue;
  width: 550px;
  display: flex;
  flex-direction: column;
}

.left-2 {
  margin: 5px;
  color: aliceblue;
  width: 530px;
  display: flex;
  flex-direction: column;
}

.col-1 {
  margin-right: 30px;
  color: aliceblue;
  width: 430px;
  display: flex;
  flex-direction: column;
}

.col-2 {
  margin-left: 30px;
  margin-right: 55px;
  color: aliceblue;
  width: 300px;
  display: flex;
  flex-direction: column;
}

.col-3 {
  margin-left: 55px;
  color: aliceblue;
  width: 540px;
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
  -ms-grid-columns: 30px 110px 60px 60px 60px 50px 100px;
  grid-template-columns: 30px 110px 60px 60px 60px 50px 100px;
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