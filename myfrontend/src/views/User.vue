<template>
  <div class="pred-container">
    <div class="left">
      <el-form ref="centerForm" status-icon :model="centerForm" :rules="rules" label-width="80px">
        <h1>个人中心</h1>
        <el-form-item label="姓名" prop="name" class="item">
          <el-input v-model="centerForm.name" style="width: 120%;"></el-input>
        </el-form-item>
        <el-form-item label="手机号" prop="phone" class="item">
          <el-input v-model="centerForm.phone" style="width: 120%;"></el-input>
        </el-form-item>
        <el-form-item label="邮箱" prop="email" class="item">
          <el-input v-model="centerForm.email" style="width: 120%;"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="updateUserInfo('centerForm')">确认</el-button>
          <!-- <el-button @click="cancel" class="button-spacing">取消</el-button> -->
        </el-form-item>
      </el-form>
    </div>
    <div class="right">
      <el-form ref="rightForm" status-icon :model="rightForm" :rules="rules" label-width="100px">
        <h1>上传鱼类数据</h1>
        <el-form-item label="品种" prop="species" class="item">
          <el-input v-model="rightForm.species" style="width: 120%;"></el-input>
        </el-form-item>
        <el-form-item label="重量(g)" prop="weight" class="item">
          <el-input v-model="rightForm.weight" style="width: 120%;"></el-input>
        </el-form-item>
        <el-form-item label="长度(cm)" prop="length" class="item">
          <el-input v-model="rightForm.length" style="width: 120%;"></el-input>
        </el-form-item>
        <el-form-item label="高度(cm)" prop="height" class="item">
          <el-input v-model="rightForm.height" style="width: 120%;"></el-input>
        </el-form-item>
        <el-form-item label="宽度(cm)" prop="width" class="item">
          <el-input v-model="rightForm.width" style="width: 120%;"></el-input>
        </el-form-item>
        <el-form-item>
          <div class="button-container">
            <el-button type="primary" @click="uploadFishData('rightForm')">上传</el-button>
            <el-button type="success" @click="exportToExcel">导出Excel</el-button>
          </div>
        </el-form-item>
      </el-form>
      <!-- <div class="top">

        <div class="content">
          <div class="title">
          </div>

        </div>

      </div>
      <div class="top bottom">

        <div class="content">
          <div class="title">
          </div>

        </div>

      </div> -->
    </div>
  </div>
</template>

<script>
import * as XLSX from 'xlsx';
import { saveAs } from 'file-saver';

export default {
  name: 'Pred',
  data() {
    return {
      centerForm: {
        name: null,
        phone: null,
        email: null,
        user: null
      },
      rightForm: {
        species: null,
        weight: null,
        length: null,
        height: null,
        width: null
      },
      rules: {
        name: [{
          required: true,
          message: '请输入姓名',
          trigger: 'blur'
        },
        {
          min: 2,
          max: 10,
          message: '长度在 2 到 8 个字符',
          trigger: 'blur'
        }
        ],
        phone: [{
          required: true,
          message: '请输入手机号',
          trigger: 'blur'
        },
        {
          pattern: /^1[34578]\d{9}$/,
          message: '手机号格式错误',
          trigger: 'blur'
        }
        ],
        email: [{
          required: true,
          message: '请输入邮箱',
          trigger: 'blur'
        },
        {
          type: 'email',
          message: '邮箱格式错误',
          trigger: 'blur'
        }
        ],
        species: [{
          required: true,
          message: '请输入品种',
          trigger: 'blur'
        }
        ],
        weight: [{
          required: true,
          message: '请输入重量',
          trigger: 'blur'
        }
        ],
        length: [{
          required: true,
          message: '请输入长度',
          trigger: 'blur'
        }
        ],
        height: [{
          required: true,
          message: '请输入高度',
          trigger: 'blur'
        }
        ],
        width: [{
          required: true,
          message: '请输入宽度',
          trigger: 'blur'
        }
        ]
      }
    }
  },
  methods: {
    updateUserInfo(formName) {
      this.$refs[formName].validate((valide) => {
        if (valide) {
          axios.patch(`/api/myApp/users/`, this.centerForm).then(res => {
            console.log(res)
            if (res.status == 200) {
              this.$message({
                message: '更新个人信息成功',
                type: 'success'
              });
              //更新缓存
              this.$store.commit("setFisherman", this.centerForm)
            } else {
              this.$message({
                type: '更新个人信息失败',
                type: 'error'
              });
            }
          }).catch(error => {
            console.log(error)
          })
        } else {
          //表单验证失败
        }
      });
    },
    uploadFishData(formName) {
      this.$refs[formName].validate((valide) => {
        if (valide) {
          axios.patch(`/api/myApp/uploadFishData/`, this.rightForm).then(res => {
            console.log(res)
            if (res.status == 200) {
              this.$message({
                message: '上传水质数据成功',
                type: 'success'
              });
              console.log("上传水质数据成功")
            } else {
              this.$message({
                type: '上传水质数据失败',
                type: 'error'
              });
            }
          }).catch(error => {
            console.log(error)
          })
        } else {
          //表单验证失败
        }
      });
    },
    async exportToExcel() {
      const response = await axios.get('/api/myApp/exportFishData/');
      if (response.status !== 200) {
        this.$message.error('导出失败');
        return;
      }
      const fishData = response.data.fish_data;
      const worksheet = XLSX.utils.json_to_sheet(fishData);
      const workbook = XLSX.utils.book_new();
      XLSX.utils.book_append_sheet(workbook, worksheet, "FishData");
      const excelBuffer = XLSX.write(workbook, { bookType: 'xlsx', type: 'array' });
      const blob = new Blob([excelBuffer], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;charset=UTF-8' });
      saveAs(blob, 'FishData.xlsx');
    }
  },
  created() {
    // console.log(this.$store.state.fisherman);
    this.centerForm = this.$store.state.fisherman;
  }
}
</script>

<style>
/* 增加按钮的上下间距并使其从上到下对齐 */
.button-container {
  display: flex;
  flex-direction: column; /* 使按钮从上到下排列 */
  gap: 20px; /* 增大按钮之间的间距 */
  align-items: flex-start; /* 从上到下对齐 */
}

.item .el-form-item__label{
    color: white;
}

.button {
  width: 100%;
  height: 30px;
  display: flex;
  justify-content: center;
}

button {
  width: 80%;
  height: 100%;
  background: #26fffd;
  color: rgb(0, 0, 0);
  border-radius: 15px;

}

.form-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 70vh;
  /* 或者根据需要设置高度 */
  margin-left: 40%;
}

.pred-container {
  display: flex;
  width: 100%;
  height: 100vh;

  .left {
    width: 800px;
    display: flex;
    flex-direction: column;
    align-items: center;

    .title {
      color: #26fffd;
      margin-top: 80px;
      font-size: 38px;
      font-weight: bold;
    }

  }

}
</style>
