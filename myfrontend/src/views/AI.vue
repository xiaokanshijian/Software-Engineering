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
                <dv-border-box-12 style="height: 300px; width: 490px ;color=white">
                  <div class="title" style="margin-top: 5px">
                    海洋牧场环境感知得分
                  </div>
                  <div style="
                      width: 100%;
                      height: 5%;
                      color: white;
                      text-align: center;
                    ">
                    <template>
                      <div class="block" style="
                          display: flex;
                          align-items: center;
                          margin-left: 10px;
                          width: 28%;
                          height: 3%;
                        ">
                        <el-date-picker v-model="date" type="date" placeholder="选择日期" size="small"
                          :picker-options="pickerOptions">
                        </el-date-picker>
                      </div>
                    </template>

                    <div style="opacity: 0.8; color: white">
                      舒适: 维持良好状态
                    </div>
                    <div style="opacity: 0.8; color: white">
                      正常: 可能出现轻微变化或趋势
                    </div>
                    <div style="opacity: 0.8; color: white">
                      隐患: 环境存在明显变化或问题
                    </div>
                    <div style="opacity: 0.8; color: white">
                      危险: 出现严重问题或危机
                    </div>
                  </div>
                  <div ref="environment_count1" style="width: 100%; height: 105%;color=white"></div>
                </dv-border-box-12>

                <dv-border-box-12 style="height: 250px; width: 490px">
                  <div class="title" style="margin-top: 5px">网衣/鱼群检测</div>
                  <div ref="secondMain" style="width: 70%; height: 100%">
                    <div ref="fishChart" style="width: 150%; height: 105%;color=white"></div>
                  </div>
                </dv-border-box-12>
              </div>
            </div>

            <div class="cent">
              <div class="col-3" style="">
                <template>
                  <dv-border-box-12 style="height: 330px; width: 540px">
                    <div style="display: flex; justify-content: space-between; width: 100%;">
                      <!-- 原始图像 -->
                      <div style="width: 50%; height: 270px; background: black; margin-top: 10px;">
                        <div class="title" style="margin-top: 5px">原始图像</div>
                        <img v-if="originalImageUrl" :src="originalImageUrl"
                          style="width: 100%; height: 100%; object-fit: cover;">
                      </div>
                      <!-- 识别效果 -->
                      <div style="width: 50%; height: 270px; background: black; margin-top: 10px;">
                        <div class="title" style="margin-top: 5px">识别效果</div>
                        <img v-if="resultImageUrl" :src="resultImageUrl"
                          style="width: 100%; height: 100%; object-fit: cover;">
                      </div>
                    </div>
                    <input type="file" @change="uploadImage" style="margin-top: 10px;">
                    <button @click="recognizeImage" style="margin-top: 10px; height: 10%; width: 20%;">图像识别</button>
                  </dv-border-box-12>
                </template>

                <dv-border-box-12 style="height: 220px; width: 540px">
                  <div class="title" style="margin-top: 5px">实时数据</div>
                  <div id="sixthMain" style="
                      display: grid;
                      grid-template-columns: repeat(3, 1fr);
                      width: 98%;
                      height: 90%;
                    ">
                    <div class="rounded-box" style="
                        display: flex;
                        flex-direction: row;
                        justify-content: flex-start;
                        align-items: center;
                      ">
                      编号
                      <camera-icon style="margin-left: auto" />
                      <span id="fishId">Fish 001</span>
                    </div>
                    <div class="rounded-box" style="
                        display: flex;
                        flex-direction: row;
                        justify-content: flex-start;
                        align-items: center;
                      ">
                      鱼种
                      <light-icon style="margin-left: auto" />
                      <span id="fishSpecies">{{ fishSpecies }}</span>
                    </div>
                    <div class="rounded-box" style="
                        display: flex;
                        flex-direction: row;
                        justify-content: flex-start;
                        align-items: center;
                      ">
                      体长
                      <brush-icon style="margin-left: auto" />
                      <span id="fishLength">10 cm</span>
                    </div>
                    <div class="rounded-box" style="
                        display: flex;
                        flex-direction: row;
                        justify-content: flex-start;
                        align-items: center;
                      ">
                      疑似病患
                      <loop-icon style="margin-left: auto" />
                      <span id="suspiciousCases">2</span>
                    </div>
                    <div class="rounded-box" style="
                        display: flex;
                        flex-direction: row;
                        justify-content: flex-start;
                        align-items: center;
                      ">
                      鱼群异常
                      <split-screen-icon style="margin-left: auto" />
                      <span id="abnormalSchools">1</span>
                    </div>
                    <div class="rounded-box" style="
                        display: flex;
                        flex-direction: row;
                        justify-content: flex-start;
                        align-items: center;
                      ">
                      轨迹分析
                      <cloud-file-icon style="margin-left: auto" />
                      <span id="trajectoryAnalysis">Available</span>
                    </div>
                  </div>
                </dv-border-box-12>
              </div>
            </div>

            <div class="right">
              <div class="col-2" style="">
                <dv-border-box-12 style="height: 300px; width: 410px">
                  <div style="
                      display: flex;
                      flex-direction: column;
                      justify-content: space-between;
                      width: 100%;
                    ">
                    <div style="
                        width: 90%;
                        height: 190px;
                        border-radius: 10px;
                        margin: 0 auto;
                      ">
                      <div class="title" style="margin-top: 5px">AI决策</div>
                      <div style="
                          display: flex;
                          flex-wrap: wrap;
                          justify-content: space-around;
                        ">
                        <div style="
                            width: 100%;
                            height: 5%;
                            color: white;
                            text-align: center;
                            font-size: 16px;
                          ">
                          <div>
                            温度：
                            <span id="temperatureValue">
                              {{ sensorData.temperature.toFixed(2) }} ℃</span>
                          </div>
                          <div>
                            光照：
                            <span id="lightValue">
                              {{ sensorData.light.toFixed(2) }} lx</span>
                          </div>
                          <div>
                            溶解氧：
                            <span id="oxygenValue">
                              {{ sensorData.oxygen.toFixed(2) }} mg/L</span>
                          </div>
                          <div>
                            盐度：
                            <span id="salinityValue">{{ sensorData.salinity.toFixed(2) }}ppt
                            </span>
                          </div>
                          <div>
                            pH：
                            <span id="phValue">{{
                              sensorData.ph.toFixed(2)
                            }}</span>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div style="width: 90%; height: 50px">
                      <div class="title" style="margin-top: 5px">提示</div>
                      <div style="
                          width: 100%;
                          height: 5%;
                          color: white;
                          text-align: center;
                          font-size: 16px;
                        ">
                        未来几天可能降雨，请保持温度风度正常
                      </div>
                      <div></div>
                    </div>
                  </div>
                </dv-border-box-12>

                <dv-border-box-12 style="height: 250px; width: 410px">
                  <div ref="fourthMain" style="width: 93%; height: 83%; margin-left: 15px">
                    <div style="
                        display: flex;
                        justify-content: space-between;
                        width: 100%;
                      ">
                      <div style="width: calc(50% - 10px); border-radius: 10px">
                        <div class="title" style="margin-top: 5px">
                          气象数据
                        </div>
                        <div id="sixthMain" style="
                            display: grid;
                            grid-template-columns: repeat(2, 1fr);
                            grid-template-rows: repeat(2, auto);
                            gap: 20px;
                          ">
                          <div class="rounded-box" style="display: flex; align-items: center">
                            温度
                            <temperature-icon style="margin-left: auto"></temperature-icon>
                            <span id="temperatureValue">20°C - 30°C</span>
                          </div>
                          <div class="rounded-box" style="display: flex; align-items: center">
                            风向
                            <wind-icon style="margin-left: auto"></wind-icon>
                            <span id="windDirection">北风</span>
                          </div>
                          <div class="rounded-box" style="display: flex; align-items: center">
                            湿度
                            <humidity-icon style="margin-left: auto"></humidity-icon>
                            <span id="humidityValue">60%</span>
                          </div>
                          <div class="rounded-box" style="display: flex; align-items: center">
                            空气污染
                            <pollution-icon style="margin-left: auto"></pollution-icon>
                            <span id="pollutionLevel">中度污染</span>
                          </div>
                        </div>
                      </div>
                      <div style="
                          width: 40%;
                          height: 5%;
                          color: white;
                          text-align: center;
                          font-size: 16px;
                        ">
                        <div class="title" style="margin-top: 5px; color: red">
                          警报
                        </div>
                        <div>
                          海啸警报
                          <span id="tsunami_alert">紧急行动通知！预计于05月12日上午10:30在沿海地区发生6级海啸。立即疏散至高处，确保安全。</span>
                          <div id="app">
                            <div>
                              <!-- 手动触发弹窗按钮 -->
                              <button @click="showAlertManually">
                                警报详细数据
                              </button>

                              <!-- 模态框 -->
                              <div v-if="isModalVisible" class="modal">
                                <div class="modal-content">
                                  <p>
                                    <strong :class="{
                                      'red-title': hasAbnormalData(),
                                      'black-title': !hasAbnormalData(),
                                    }">
                                      {{
                                        hasAbnormalData()
                                          ? "警报"
                                          : "当前传感器数据"
                                      }}
                                    </strong>
                                  </p>
                                  <p :class="getTextClass(
                                    sensorData.temperature,
                                    temperatureRange
                                  )
                                    ">
                                    温度:
                                    {{ sensorData.temperature.toFixed(2) }} ℃
                                    (预设区间: {{ temperatureRange.min }} -
                                    {{ temperatureRange.max }} ℃)
                                  </p>
                                  <p :class="getTextClass(sensorData.light, lightRange)
                                    ">
                                    光照: {{ sensorData.light.toFixed(2) }} lx
                                    (预设区间: {{ lightRange.min }} -
                                    {{ lightRange.max }} lx)
                                  </p>
                                  <p :class="getTextClass(
                                    sensorData.oxygen,
                                    oxygenRange
                                  )
                                    ">
                                    溶解氧:
                                    {{ sensorData.oxygen.toFixed(2) }} mg/L
                                    (预设区间: {{ oxygenRange.min }} -
                                    {{ oxygenRange.max }} mg/L)
                                  </p>
                                  <p :class="getTextClass(
                                    sensorData.salinity,
                                    salinityRange
                                  )
                                    ">
                                    盐度:
                                    {{ sensorData.salinity.toFixed(2) }} ppt
                                    (预设区间: {{ salinityRange.min }} -
                                    {{ salinityRange.max }} ppt)
                                  </p>
                                  <p :class="getTextClass(sensorData.ph, phRange)
                                    ">
                                    pH:
                                    {{ sensorData.ph.toFixed(2) }} (预设区间:
                                    {{ phRange.min }} - {{ phRange.max }})
                                  </p>
                                  <p :class="getTextClass(
                                    sensorData.fishCount,
                                    fishCountRange
                                  )
                                    ">
                                    鱼群数量:
                                    {{ sensorData.fishCount.toFixed(2) }}
                                    (预设区间: {{ fishCountRange.min }} -
                                    {{ fishCountRange.max }})
                                  </p>
                                  <p :class="getTextClass(
                                    sensorData.fishActivity,
                                    fishActivityRange
                                  )
                                    ">
                                    鱼群活跃度:
                                    {{ sensorData.fishActivity.toFixed(2) }}
                                    (预设区间: {{ fishActivityRange.min }} -
                                    {{ fishActivityRange.max }})
                                  </p>
                                  <p :class="getEnvironmentScoreClass()">
                                    智能环境评分:
                                    {{ environmentScore.toFixed(2) }}
                                    <span>{{ getEnvironmentScoreText() }}</span>
                                  </p>
                                  <button @click="hideAlert">关闭</button>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
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
      pickerOptions: {
        disabledDate(time) {
          return !(
            (time.getTime() >= new Date("2024-4-11") &&
              time.getTime() <= new Date("2024-4-16")) ||
            (time.getTime() >= new Date("2024-5-11") &&
              time.getTime() <= new Date("2024-5-15"))
          );
        },
      },
      date: new Date("2024-04-11"),
      scores: {},

      //报警部分所用到的所有数据，在处理函数中暂定为随机数
      isModalVisible: false,
      //环境各项指标
      sensorData: {
        temperature: 0,
        light: 0,
        oxygen: 0,
        salinity: 0,
        ph: 0,
        fishCount: 0,
        fishActivity: 0,
      },
      //环境加权得分
      environmentScore: 0,
      //各项指标范围
      temperatureRange: { min: 15, max: 35 },
      lightRange: { min: 200, max: 800 },
      oxygenRange: { min: 5, max: 9 },
      salinityRange: { min: 10, max: 30 },
      phRange: { min: 6.5, max: 8.5 },
      fishCountRange: { min: 50, max: 500 },
      fishActivityRange: { min: 1, max: 10 },
      environmentScoreRange: { min: 0, max: 100 },
      //环境加权评分权重
      weights: {
        temperature: 0.2,
        light: 0.1,
        oxygen: 0.2,
        salinity: 0.15,
        ph: 0.15,
        fishCount: 0.1,
        fishActivity: 0.1,
      },
      originalImageUrl: null,
      resultImageUrl: null,
      fishSpecies: "Goldfish",
    };
  },
  watch: {
    date(newDate) {
      this.environment_point();
    },
  },
  methods: {
    environment_point() {
      $(document).ready(() => {
        var chartDom = this.$refs.environment_count1;
        var myChart = this.$echarts.init(chartDom);
        var option;
        var selectedMonth = this.date.getMonth() + 1; // getMonth() 返回的月份从 0 开始
        var selectedDate = this.date.getDate();
        var score = this.scores[selectedMonth][selectedDate];

        option = {
          series: [
            {
              type: "gauge",
              startAngle: 180,
              endAngle: 0,
              center: ["50%", "75%"],
              radius: "90%",
              min: 0,
              max: 1,
              splitNumber: 8,
              axisLine: {
                lineStyle: {
                  width: 6,
                  color: [
                    [0.25, "#FF6E76"],
                    [0.5, "#FDDD60"],
                    [0.75, "#58D9F9"],
                    [1, "#7CFFB2"],
                  ],
                },
              },
              pointer: {
                icon: "path://M12.8,0.7l12,40.1H0.7L12.8,0.7z",
                length: "12%",
                width: 20,
                offsetCenter: [0, "-60%"],
                itemStyle: {
                  color: "auto",
                },
              },
              axisTick: {
                length: 12,
                lineStyle: {
                  color: "auto",
                  width: 2,
                },
              },
              splitLine: {
                length: 20,
                lineStyle: {
                  color: "auto",
                  width: 5,
                },
              },
              axisLabel: {
                color: "#464646",
                fontSize: 20,
                distance: -60,
                rotate: "tangential",
                formatter: function (value) {
                  if (value === 0.875) {
                    return "舒适";
                  } else if (value === 0.625) {
                    return "正常";
                  } else if (value === 0.375) {
                    return "隐患";
                  } else if (value === 0.125) {
                    return "危险";
                  }
                  return "";
                },
                textStyle: {
                  color: "white",
                },
              },
              title: {
                offsetCenter: [0, "-10%"],
                fontSize: 20,
                color: "white",
              },
              detail: {
                fontSize: 30,
                offsetCenter: [0, "-35%"],
                valueAnimation: true,
                formatter: function (value) {
                  return Math.round(value) + "";
                },
                color: "inherit",
              },
              data: [
                {
                  value: score,
                  name: "环境评估",
                },
              ],
            },
          ],
        };

        option && myChart.setOption(option);
      });
    },
    setFishdata() {
      $(document).ready(() => {
        var chartDom = this.$refs.fishChart;
        var myChart = this.$echarts.init(chartDom);
        var option;

        // prettier-ignore
        const data = [["2000-06-05", 116], ["2000-06-06", 129], ["2000-06-07", 135], ["2000-06-08", 86], ["2000-06-09", 73], ["2000-06-10", 85], ["2000-06-11", 73], ["2000-06-12", 68], ["2000-06-13", 92], ["2000-06-14", 130], ["2000-06-15", 245], ["2000-06-16", 139], ["2000-06-17", 115], ["2000-06-18", 111], ["2000-06-19", 309], ["2000-06-20", 206], ["2000-06-21", 137], ["2000-06-22", 128], ["2000-06-23", 85], ["2000-06-24", 94], ["2000-06-25", 71], ["2000-06-26", 106], ["2000-06-27", 84], ["2000-06-28", 93], ["2000-06-29", 85], ["2000-06-30", 73], ["2000-07-01", 83], ["2000-07-02", 125], ["2000-07-03", 107], ["2000-07-04", 82], ["2000-07-05", 44], ["2000-07-06", 72], ["2000-07-07", 106], ["2000-07-08", 107], ["2000-07-09", 66], ["2000-07-10", 91], ["2000-07-11", 92], ["2000-07-12", 113], ["2000-07-13", 107], ["2000-07-14", 131], ["2000-07-15", 111], ["2000-07-16", 64], ["2000-07-17", 69], ["2000-07-18", 88], ["2000-07-19", 77], ["2000-07-20", 83], ["2000-07-21", 111], ["2000-07-22", 57], ["2000-07-23", 55], ["2000-07-24", 60]];
        const dateList = data.map(function (item) {
          return item[0];
        });
        const valueList = data.map(function (item) {
          return item[1];
        });
        option = {
          visualMap: [
            {
              show: false,
              type: "continuous",
              seriesIndex: 0,
              min: 0,
              max: 400,
            },
            {
              show: false,
              type: "continuous",
              seriesIndex: 1,
              dimension: 0,
              min: 0,
              max: dateList.length - 1,
            },
          ],
          title: [
            {
              left: "center",
              text: "鱼群数量",
              textStyle: {
                color: "#ffffff",
              },
            },
            {
              top: "55%",
              left: "center",
              text: "鱼群活跃度",
              textStyle: {
                color: "#ffffff",
              },
            },
          ],
          tooltip: {
            trigger: "axis",
          },
          xAxis: [
            {
              data: dateList,
            },
            {
              data: dateList,
              gridIndex: 1,
            },
          ],
          yAxis: [
            {},
            {
              gridIndex: 1,
            },
          ],
          grid: [
            {
              bottom: "60%",
            },
            {
              top: "60%",
            },
          ],
          series: [
            {
              type: "line",
              showSymbol: false,
              data: valueList,
            },
            {
              type: "line",
              showSymbol: false,
              data: valueList,
              xAxisIndex: 1,
              yAxisIndex: 1,
            },
          ],
        };

        option && myChart.setOption(option);
      });
    },
    showAlertManually() {
      this.updateSensorData();
      this.isModalVisible = true;
    },
    hideAlert() {
      this.isModalVisible = false;
    },
    updateSensorData() {
      // 模拟传感器数据
      this.sensorData.temperature = Math.random() * 40;
      this.sensorData.light = Math.random() * 1000;
      this.sensorData.oxygen = Math.random() * 10;
      this.sensorData.salinity = Math.random() * 35;
      this.sensorData.ph = Math.random() * 14;
      this.sensorData.fishCount = Math.random() * 600;
      this.sensorData.fishActivity = Math.random() * 12;

      // 更新加权环境得分
      this.environmentScore = this.calculateEnvironmentScore();

      // 检查是否有异常数据
      if (this.hasAbnormalData()) {
        this.isModalVisible = true;
      }
    },
    hasAbnormalData() {
      return (
        !this.isWithinRange(
          this.sensorData.temperature,
          this.temperatureRange
        ) ||
        !this.isWithinRange(this.sensorData.light, this.lightRange) ||
        !this.isWithinRange(this.sensorData.oxygen, this.oxygenRange) ||
        !this.isWithinRange(this.sensorData.salinity, this.salinityRange) ||
        !this.isWithinRange(this.sensorData.ph, this.phRange) ||
        !this.isWithinRange(this.sensorData.fishCount, this.fishCountRange) ||
        !this.isWithinRange(
          this.sensorData.fishActivity,
          this.fishActivityRange
        ) ||
        !this.isWithinRange(this.environmentScore, this.environmentScoreRange)
      );
    },
    isWithinRange(value, range) {
      return value >= range.min && value <= range.max;
    },
    getTextClass(value, range) {
      return this.isWithinRange(value, range) ? "black-text" : "red-text";
    },
    getEnvironmentScoreClass() {
      if (this.environmentScore < 25) {
        return "red-score";
      } else if (this.environmentScore < 50) {
        return "yellow-score";
      } else if (this.environmentScore < 75) {
        return "blue-score";
      } else {
        return "green-score";
      }
    },
    getEnvironmentScoreText() {
      if (this.environmentScore < 25) {
        return "危险";
      } else if (this.environmentScore < 50) {
        return "隐患";
      } else if (this.environmentScore < 75) {
        return "正常";
      } else {
        return "舒适";
      }
    },
    calculateEnvironmentScore() {
      const normalizedTemperature = this.calculateNormalizedScore(
        this.sensorData.temperature,
        this.temperatureRange
      );
      const normalizedLight = this.calculateNormalizedScore(
        this.sensorData.light,
        this.lightRange
      );
      const normalizedOxygen = this.calculateNormalizedScore(
        this.sensorData.oxygen,
        this.oxygenRange
      );
      const normalizedSalinity = this.calculateNormalizedScore(
        this.sensorData.salinity,
        this.salinityRange
      );
      const normalizedPh = this.calculateNormalizedScore(
        this.sensorData.ph,
        this.phRange
      );
      const normalizedFishCount = this.calculateNormalizedScore(
        this.sensorData.fishCount,
        this.fishCountRange
      );
      const normalizedFishActivity = this.calculateNormalizedScore(
        this.sensorData.fishActivity,
        this.fishActivityRange
      );

      // 将每个归一化后的指标乘以相应的权重，然后计算总得分
      const totalScore =
        (normalizedTemperature * this.weights.temperature +
          normalizedLight * this.weights.light +
          normalizedOxygen * this.weights.oxygen +
          normalizedSalinity * this.weights.salinity +
          normalizedPh * this.weights.ph +
          normalizedFishCount * this.weights.fishCount +
          normalizedFishActivity * this.weights.fishActivity) /
        (this.weights.temperature +
          this.weights.light +
          this.weights.oxygen +
          this.weights.salinity +
          this.weights.ph +
          this.weights.fishCount +
          this.weights.fishActivity);

      return totalScore * 100;
    },

    calculateNormalizedScore(value, range) {
      const midPoint = (range.min + range.max) / 2;
      const deviation = Math.abs(value - midPoint);
      const maxDeviation = (range.max - range.min) / 2;

      let normalizedScore = 1 - deviation / maxDeviation;
      normalizedScore = Math.max(0, Math.min(1, normalizedScore));

      return normalizedScore;
    },
    uploadImage(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          this.originalImageUrl = e.target.result;
        };
        reader.readAsDataURL(file);
      }
    },
    // Base64字符串转Blob对象的辅助函数
    base64ToBlob(base64) {
      const byteString = atob(base64.split(',')[1]);
      const mimeString = base64.split(',')[0].split(':')[1].split(';')[0];
      const ab = new ArrayBuffer(byteString.length);
      const ia = new Uint8Array(ab);
      for (let i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i);
      }
      return new Blob([ab], { type: mimeString });
    },
    async recognizeImage() {
      if (!this.originalImageUrl) {
        alert("请先上传原始图像");
        return;
      }
      try {
        const response = await fetch(this.originalImageUrl);
        const blob = await response.blob();
        const formData = new FormData();
        formData.append('image', blob, 'image.png');
        // 使用axios发送POST请求到后端，并请求返回图像和result_category
        const axiosResponse = await axios.post(`myApp/AICenter/`, formData, {
          responseType: 'json', // 修改响应类型为json以接收图像和result_category
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
        // 假设后端返回的图像数据是Base64编码的字符串
        // const base64Image = axiosResponse.data.image_data; // 获取返回的图像Base64编码字符串
        // 将Base64编码的字符串转换为Blob对象
        // const resultBlob = this.base64ToBlob(base64Image);
        const resultCategory = axiosResponse.data.result_category; // 获取返回的分类结果
        // 创建一个URL对象并更新resultImageUrl以显示识别后的图像
        const imageData = axiosResponse.data.image_data;
        // 将Base64编码的图像数据设置为图像源
        this.resultImageUrl = `data:image/png;base64,${imageData}`;
        // 可以在此处处理resultCategory，例如更新UI显示分类结果
        console.log("识别结果分类：", resultCategory);
        this.fishSpecies = resultCategory;
      } catch (error) {
        console.error("识别图像时出错：", error);
        alert("识别图像时出错");
      }
    }
  },
  async created() {
    const response = await axios.get(`myApp/underwaterSystem/`);
    this.$set(this.scores, "4", response.data.scores.April);
    this.$set(this.scores, "5", response.data.scores.May);
    $(document).ready(async () => {
      this.setFishdata();
      this.environment_point();
    });
  },
  //警报系统，短轮询更新数据，由于这里的指标是随机数，容易触发报警，此时设定的是200s检查一次
  mounted() {
    setInterval(() => {
      this.updateSensorData();
    }, 200000);
  },
  components: {
    LeftTop,
  },
};
</script>
<style lang="less" scoped>
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

.app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

//警告框风格
.modal {
  display: block;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.4);
}

.modal-content {
  background-color: #fefefe;
  margin: 15% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
  max-width: 300px;
  text-align: center;
}

.red-text {
  color: red;
}

.black-text {
  color: black;
}

.red-title {
  color: red;
  font-size: 24px;
}

.black-title {
  color: black;
  font-size: 24px;
}

.red-score {
  color: rgb(178, 34, 34);
  font-size: 32px;
}

.yellow-score {
  color: rgb(218, 165, 32);
  font-size: 32px;
}

.blue-score {
  color: rgb(0, 51, 102);
  font-size: 32px;
}

.green-score {
  color: rgb(34, 139, 34);
  font-size: 32px;
}
</style>
