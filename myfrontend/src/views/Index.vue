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

                <dv-border-box-12 style="height: 350px; width: 490px">
                  <div class="title" style="margin-top: 5px">
                    历史记录
                  </div>

                  <template>
                    <div class="block" style="display: flex; align-items: center; margin-left: 150px; width: 30%; color: #4b83f2;">
                      <el-date-picker v-model="date" type="date" placeholder="选择日期" size="small" :picker-options="pickerOptions">
                      </el-date-picker>
                    </div>
                  </template>

                  <div ref="firstMain" style="width: 100%; height: 90%"></div>
                </dv-border-box-12>

                <dv-border-box-12 style="height: 200px; width: 490px">
                  <div class="title" style="margin-top: 5px">
                    设备状态
                  </div>
                  <!-- <div ref="secondMain" style="width: 70%; height: 100%"> -->
                  <template>
                    <el-tabs v-model="activeName" @tab-click="handleClick"
                      style="margin-left: 50px; margin-right: 50px;">
                      <el-tab-pane label="主控" name="first">主控</el-tab-pane>
                      <el-tab-pane label="时间校准" name="second">时间校准</el-tab-pane>
                      <el-tab-pane label="通道" name="third">通道</el-tab-pane>
                      <el-tab-pane label="告警" name="fourth">告警</el-tab-pane>
                    </el-tabs>
                  </template>
                  <!-- </div> -->
                </dv-border-box-12>



              </div>
            </div>

            <div class="cent">
              <div class="col-2" style="">

                <dv-border-box-12 style="height: 300px; width: 410px">
                  <div class="title" style="margin-top: 5px">
                    水文气象
                  </div>
                  <template>
                    <el-tabs v-model="activeName3" @tab-click="handleClick3"
                      style="margin-left: 25px; margin-right: 15px;">
                      <el-tab-pane label="Ⅰ类" name="first">
                        <div ref="secondMain" style="width: 100%; height: 250px"></div>
                      </el-tab-pane>
                      <el-tab-pane label="Ⅱ类" name="second">
                        <div ref="thirdMain" style="width: 380px; height: 250px"></div>
                      </el-tab-pane>
                      <el-tab-pane label="Ⅲ类" name="third">
                        <div ref="fourthMain" style="width: 100%; height: 250px"></div>
                      </el-tab-pane>
                      <el-tab-pane label="Ⅳ类" name="fourth">
                        <div ref="fifthMain" style="width: 100%; height: 250px"></div>
                      </el-tab-pane>
                      <el-tab-pane label="Ⅴ类" name="fith">
                        <div ref="sixthMain" style="width: 100%; height: 250px"></div>
                      </el-tab-pane>
                    </el-tabs>
                  </template>

                  <!-- <div ref="thirdMain" style="width: 100%; height: 100%"></div> -->
                </dv-border-box-12>

                <dv-border-box-12 style="height: 250px; width: 410px">
                  <div class="title" style="margin-top: 5px">
                    定位
                  </div>
                  <!-- <div ref="fourthMain" style="width: 93%; height: 83%; margin-left: 15px"> -->
                  <template>
                    <div id="map" style="width: 93%; height: 83%; margin-left: 15px"></div>
                  </template>
                  <!-- </div> -->
                </dv-border-box-12>

              </div>
            </div>

            <div class="right">
              <div class="col-3" style="">
                <dv-border-box-12 style="height: 330px; width: 540px">
                  <div class="title" style="margin-top: 5px">
                    监控视频
                  </div>

                  <template>
                    <!-- <div id="fifthMain" style="width: 85%; height: 150px"> -->
                    <el-tabs v-model="activeName2" @tab-click="handleClick2"
                      style="margin-left: 50px; margin-right: 50px;">
                      <el-tab-pane v-for="(video, index) in videos" :label="video.label" :name="video.name"
                        :key="index">
                        <video :src="video.src" controls style="width: 95%; height: 90%"></video>
                      </el-tab-pane>
                    </el-tabs>
                    <!-- </div> -->
                  </template>
                </dv-border-box-12>

                <dv-border-box-12 style="height: 220px; width: 540px">
                  <div class="title" style="margin-top: 5px">
                    附加功能
                  </div>
                  <div style="display: grid; grid-template-columns: repeat(3, 1fr); width: 98%; height: 90%">
                    <div class="rounded-box"
                      style="display: flex; flex-direction: row; justify-content: flex-start; align-items: center;">
                      摄像头
                      <camera-icon style="margin-left: auto;" />
                    </div>
                    <div class="rounded-box"
                      style="display: flex; flex-direction: row; justify-content: flex-start; align-items: center;">
                      灯光
                      <light-icon style="margin-left: auto;" />
                    </div>
                    <div class="rounded-box"
                      style="display: flex; flex-direction: row; justify-content: flex-start; align-items: center;">
                      清洁
                      <brush-icon style="margin-left: auto;" />
                    </div>
                    <div class="rounded-box"
                      style="display: flex; flex-direction: row; justify-content: flex-start; align-items: center;">
                      回放
                      <loop-icon style="margin-left: auto;" />
                    </div>
                    <div class="rounded-box"
                      style="display: flex; flex-direction: row; justify-content: flex-start; align-items: center;">
                      同时播放
                      <split-screen-icon style="margin-left: auto;" />
                    </div>
                    <div class="rounded-box"
                      style="display: flex; flex-direction: row; justify-content: flex-start; align-items: center;">
                      云台摄像机
                      <cloud-file-icon style="margin-left: auto;" />
                    </div>
                  </div>
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
import CameraIcon from "@/components/CameraIcon.vue";
import LightIcon from "@/components/LightIcon.vue";
import BrushIcon from "@/components/BrushIcon.vue";
import LoopIcon from "@/components/LoopIcon.vue";
import SplitScreenIcon from "@/components/SplitScreenIcon.vue";
import CloudFileIcon from "@/components/CloudFileIcon.vue";
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
      activeName: "first",
      activeName2: "first",
      activeName3: "first",
      videos: [
        { label: '视频1', name: 'first', src: '/videos/video1.mp4' },
        { label: '视频2', name: 'second', src: '/videos/video2.mp4' },
        { label: '视频3', name: 'third', src: '/videos/video3.mp4' },
        { label: '视频4', name: 'fourth', src: '/videos/video4.mp4' },
      ],
      records: {},
      temperature: {},
      ph: {},
      dissolved_oxygen: {},
      conductivity: {},
      turbidity: {},
      permanganate_index: {},
      ammonia_nitrogen: {},
      total_nitrogen: {},
      total_phosphorus: {},
      pickerOptions: {
        disabledDate(time) {
          return !((time.getTime() >= new Date('2024-4-11') && time.getTime() <= new Date('2024-4-16'))
          || (time.getTime() >= new Date('2024-5-11') && time.getTime() <= new Date('2024-5-15')));
        },
      },
      date: new Date('2024-04-11'),
    };
  },
  watch: {
    date(newDate) {
      console.log(newDate); // 当 date 的值改变时，打印新的值
      this.setBarData();
      this.setBarData2();
    },
  },
  mounted() {
    // 百度地图API功能
    if (typeof BMap !== 'undefined') {
      // BMap存在，执行相关操作
      var map = new BMap.Map("map");
      var point = new BMap.Point(116.404, 39.915);
      map.centerAndZoom(point, 15);
      map.enableScrollWheelZoom(true);
      // 设置地图类型为混合地图
      map.setMapType(BMAP_HYBRID_MAP);
      // 其他与BMap相关的代码
    } else {
      // BMap不存在，可能是在测试环境中
      console.log("BMap is not defined.");
    }
  },
  methods: {
    setBarData() {
      $(document).ready(() => {
        var chartDom = this.$refs.firstMain;
        var myChart = this.$echarts.init(chartDom);
        var selectedMonth = this.date.getMonth() + 1; // getMonth() 返回的月份从 0 开始
        var selectedDate = this.date.getDate();
        var option = {
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
              dataView: { show: true, readOnly: false },
              magicType: { show: false, type: ['line', 'bar'] },
              restore: { show: true },
              saveAsImage: { show: false }
            }
          },
          legend: {
            // data: ['氨氮(mg/L)', '总磷(mg/L)', '总氮(mg/L)'],
            textStyle: {
              color: '#ffffff',
            }
          },
          xAxis: [
            {
              type: 'category',
              data: ['Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ'],
              axisLabel: {
                color: '#ffffff',
                fontSize: 10
              },
              axisPointer: {
                type: 'shadow'
              },
              show: true
            }
          ],
          yAxis: [
            {
              type: 'value',
              name: '氨氮含量',
              nameTextStyle: {
                color: '#ffffff',
              },
              min: 0,
              max: 0.5,
              interval: 0.1,
              axisLabel: {
                color: '#ffffff',
                fontSize: 10
              }
            },
            {
              type: 'value',
              name: '数量/浊度',
              nameTextStyle: {
                color: '#ffffff'
              },
              min: 0,
              max: 100,
              interval: 20,
              axisLabel: {
                color: '#ffffff',
                fontSize: 10
              }
            }
          ],
          series: [
            {
              name: '记录数量',
              type: 'bar',
              yAxisIndex: 1,
              data: this.records[selectedMonth][selectedDate],
            },
            {
              name: '浊度(NTU)',
              type: 'bar',
              yAxisIndex: 1,
              tooltip: {
                valueFormatter: function (value) {
                  return value + 'NTU';
                }
              },
              data: this.turbidity[selectedMonth][selectedDate][0],
            },
            {
              name: '氨氮(mg/L)',
              type: 'line',
              tooltip: {
                valueFormatter: function (value) {
                  return value + 'mg/L';
                }
              },
              data: this.ammonia_nitrogen[selectedMonth][selectedDate][0],
            },
            {
              name: '总氮(mg/L)',
              type: 'line',
              tooltip: {
                valueFormatter: function (value) {
                  return value + 'mg/L';
                }
              },
              data: this.total_nitrogen[selectedMonth][selectedDate][0],
            }
          ]
        };

        option && myChart.setOption(option);
      });
    },
    setBarData2() {
      $(document).ready(() => {
        // console.log(this.activeName3);
        var unit = ['μS/cm', 'mg/L', 'mg/L', 'mg/L', '', '°C'];
        var chartDom, realData, displayData;
        var selectedMonth = this.date.getMonth() + 1; // getMonth() 返回的月份从 0 开始
        var selectedDate = this.date.getDate();
        if (this.activeName3 == 'first') {
          chartDom = this.$refs.secondMain;
          realData = [this.conductivity[selectedMonth][selectedDate][0][0], this.permanganate_index[selectedMonth][selectedDate][0][0], this.dissolved_oxygen[selectedMonth][selectedDate][0][0], this.total_nitrogen[selectedMonth][selectedDate][0][0], this.ph[selectedMonth][selectedDate][0][0], this.temperature[selectedMonth][selectedDate][0][0]];
          displayData = [this.conductivity[selectedMonth][selectedDate][1][0], this.permanganate_index[selectedMonth][selectedDate][1][0], this.dissolved_oxygen[selectedMonth][selectedDate][1][0], this.total_nitrogen[selectedMonth][selectedDate][1][0], this.ph[selectedMonth][selectedDate][1][0], this.temperature[selectedMonth][selectedDate][1][0]];
        } else if (this.activeName3 == 'second') {
          realData = [this.conductivity[selectedMonth][selectedDate][0][1], this.permanganate_index[selectedMonth][selectedDate][0][1], this.dissolved_oxygen[selectedMonth][selectedDate][0][1], this.total_nitrogen[selectedMonth][selectedDate][0][1], this.ph[selectedMonth][selectedDate][0][1], this.temperature[selectedMonth][selectedDate][0][1]];
          displayData = [this.conductivity[selectedMonth][selectedDate][1][1], this.permanganate_index[selectedMonth][selectedDate][1][1], this.dissolved_oxygen[selectedMonth][selectedDate][1][1], this.total_nitrogen[selectedMonth][selectedDate][1][1], this.ph[selectedMonth][selectedDate][1][1], this.temperature[selectedMonth][selectedDate][1][1]];
          chartDom = this.$refs.thirdMain;
        } else if (this.activeName3 == 'third') {
          realData = [this.conductivity[selectedMonth][selectedDate][0][2], this.permanganate_index[selectedMonth][selectedDate][0][2], this.dissolved_oxygen[selectedMonth][selectedDate][0][2], this.total_nitrogen[selectedMonth][selectedDate][0][2], this.ph[selectedMonth][selectedDate][0][2], this.temperature[selectedMonth][selectedDate][0][2]];
          displayData = [this.conductivity[selectedMonth][selectedDate][1][2], this.permanganate_index[selectedMonth][selectedDate][1][2], this.dissolved_oxygen[selectedMonth][selectedDate][1][2], this.total_nitrogen[selectedMonth][selectedDate][1][2], this.ph[selectedMonth][selectedDate][1][2], this.temperature[selectedMonth][selectedDate][1][2]];
          chartDom = this.$refs.fourthMain;
        } else if (this.activeName3 == 'fourth') {
          realData = [this.conductivity[selectedMonth][selectedDate][0][3], this.permanganate_index[selectedMonth][selectedDate][0][3], this.dissolved_oxygen[selectedMonth][selectedDate][0][3], this.total_nitrogen[selectedMonth][selectedDate][0][3], this.ph[selectedMonth][selectedDate][0][3], this.temperature[selectedMonth][selectedDate][0][3]];
          displayData = [this.conductivity[selectedMonth][selectedDate][1][3], this.permanganate_index[selectedMonth][selectedDate][1][3], this.dissolved_oxygen[selectedMonth][selectedDate][1][3], this.total_nitrogen[selectedMonth][selectedDate][1][3], this.ph[selectedMonth][selectedDate][1][3], this.temperature[selectedMonth][selectedDate][1][3]];
          chartDom = this.$refs.fifthMain;
        } else if (this.activeName3 == 'fith') {
          realData = [this.conductivity[selectedMonth][selectedDate][0][4], this.permanganate_index[selectedMonth][selectedDate][0][4], this.dissolved_oxygen[selectedMonth][selectedDate][0][4], this.total_nitrogen[selectedMonth][selectedDate][0][4], this.ph[selectedMonth][selectedDate][0][4], this.temperature[selectedMonth][selectedDate][0][4]];
          displayData = [this.conductivity[selectedMonth][selectedDate][1][4], this.permanganate_index[selectedMonth][selectedDate][1][4], this.dissolved_oxygen[selectedMonth][selectedDate][1][4], this.total_nitrogen[selectedMonth][selectedDate][1][4], this.ph[selectedMonth][selectedDate][1][4], this.temperature[selectedMonth][selectedDate][1][4]];
          chartDom = this.$refs.sixthMain;
        }

        var myChart = this.$echarts.init(chartDom);
        var option = {
          tooltip: {
            trigger: "axis",
            axisPointer: {
              type: "shadow"
            },
            formatter: function (params) {
              return params[0].name + "<br/>" + params[1].axisValue + unit[params[0].dataIndex];
            }
          },
          grid: {
            top: "1%",
            left: "25%",
            right: "18%",
            bottom: "15%"
            // containLabel: true
          },
          // 不显示x轴的相关信息
          xAxis: {
            show: false
          },
          yAxis: [
            {
              type: "category",
              inverse: true,
              data: ["电导率", "高锰酸盐指数", "溶解氧", "总氮", "pH", "水温"],
              // 不显示y轴的线
              axisLine: {
                show: false
              },
              // 不显示刻度
              axisTick: {
                show: false
              },
              // 把刻度标签里面的文字颜色设置为白色
              axisLabel: {
                color: "#fff",
                fontSize: 14,
              }
            },
            {
              data: realData,
              inverse: true,
              // 不显示y轴的线
              axisLine: {
                show: false
              },
              // 不显示刻度
              axisTick: {
                show: false
              },
              // 把刻度标签里面的文字颜色设置为白色
              axisLabel: {
                color: "#fff",
                formatter: function (value, index) {
                  return parseFloat(value).toFixed(2);
                }
              }
            }
          ],
          series: [
            {
              name: "条",
              type: "bar",
              data: displayData,
              yAxisIndex: 0,
              // 修改第一组柱子的圆角
              itemStyle: {
                barBorderRadius: 20,
                // 此时的color 可以修改柱子的颜色
                color: '#00A86B'
              },
              // 柱子之间的距离
              barCategoryGap: 50,
              //柱子的宽度
              barWidth: 10,
              // 显示柱子内的文字
              label: {
                show: false,
                position: "inside",
                // {c} 会自动的解析为 数据  data里面的数据
                formatter: "{c}%"
              },
            },
            {
              name: "框",
              type: "bar",
              barCategoryGap: 50,
              barWidth: 15,
              yAxisIndex: 1,
              data: [100, 100, 100, 100, 100, 100],
              itemStyle: {
                color: "none", // 不要条的颜色
                borderColor: "#00c1de",
                borderWidth: 3,
                barBorderRadius: 15
              }
            }
          ]
        };

        option && myChart.setOption(option);
      });
    },
    handleClick(tab, event) {
      // console.log(tab, event);
    },
    handleClick2(tab, event) {
      // console.log(tab, event);
    },
    handleClick3(tab, event) {
      // console.log(tab, event);
      this.setBarData2();
    },
    setHydrodata(response) {
      // console.log(response.data.April);
      this.$set(this.records, '4', response.data.records.April);
      this.$set(this.records, '5', response.data.records.May);
      this.$set(this.temperature, '4', response.data.April.temperature);
      this.$set(this.temperature, '5', response.data.May.temperature);
      this.$set(this.ph, '4', response.data.April.ph);
      this.$set(this.ph, '5', response.data.May.ph);
      this.$set(this.dissolved_oxygen, '4', response.data.April.dissolved_oxygen);
      this.$set(this.dissolved_oxygen, '5', response.data.May.dissolved_oxygen);
      this.$set(this.conductivity, '4', response.data.April.conductivity);
      this.$set(this.conductivity, '5', response.data.May.conductivity);
      this.$set(this.turbidity, '4', response.data.April.turbidity);
      this.$set(this.turbidity, '5', response.data.May.turbidity);
      this.$set(this.permanganate_index, '4', response.data.April.permanganate_index);
      this.$set(this.permanganate_index, '5', response.data.May.permanganate_index);
      this.$set(this.ammonia_nitrogen, '4', response.data.April.ammonia_nitrogen);
      this.$set(this.ammonia_nitrogen, '5', response.data.May.ammonia_nitrogen);
      this.$set(this.total_nitrogen, '4', response.data.April.total_nitrogen);
      this.$set(this.total_nitrogen, '5', response.data.May.total_nitrogen);
      this.$set(this.total_phosphorus, '4', response.data.April.total_phosphorus);
      this.$set(this.total_phosphorus, '5', response.data.May.total_phosphorus);
      // console.log(this.records.April);
      // console.log(this.total_nitrogen.April);
    }
  },
  async created() {
    $(document).ready(async () => {
      const response = await axios.get(`myApp/main/`);
      this.setHydrodata(response);
      this.setBarData()
      this.setBarData2()
    })
  },
  components: {
    LeftTop,
    CameraIcon,
    LightIcon,
    BrushIcon,
    LoopIcon,
    SplitScreenIcon,
    CloudFileIcon
  },
};
</script>

<style lang="less" scoped>
.center-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh; /* 设置容器的高度为视口的高度，这样组件就会在垂直方向上居中 */
}

.custom-date-picker {
  color: #4b83f2; //当前标签页颜色
  margin-left: 50px; /* 向右移动50px */
}

#sixthMain {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.rounded-box {
  background-color: rgb(7, 76, 140);
  /* 天蓝色背景 */
  border-radius: 10px;
  /* 圆角 */
  color: white;
  /* 白色文字 */
  font-size: 15px;
  /* 字体大小 */
  font-weight: bold;
  /* 字体加粗 */
  padding: 20px;
  /* 内边距 */
  width: calc(63.33% - 5px);
  /* 设置盒子的宽度，使得每行可以放置三个盒子 */
  margin-bottom: 8px;
  /* 添加底部边距，使得两行之间有空间 */
  height: 35px;
  margin-left: 12%;
  margin-top: 8px;
}

::v-deep .el-tabs__item.is-active {
  color: #4b83f2; //当前标签页颜色
}

::v-deep .el-tabs__item {
  color: #bfc0c2; //标签页默认颜色
  font-weight: bold;
  font-size: 15px;
}

::v-deep .el-tabs__item:hover {
  color: #bfc0c2; //鼠标悬停标签页变化的颜色
}

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