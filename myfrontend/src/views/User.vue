<template>
  <div class="pred-container">
    <div class="form-container">
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
          <el-button type="primary" @click="updateInfo('centerForm')">确认</el-button>
          <!-- <el-button @click="cancel" class="button-spacing">取消</el-button> -->
        </el-form-item>
      </el-form>
    </div>
    <!-- <div class="left">
      <div class="title">
        <img src="../assets/logo.png" style="width:80px;height:80px;" alt="">
        LOGO
      </div>

    </div>
    <div class="right">
      <div class="top">

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

      </div>
    </div> -->
  </div>
</template>

<script>
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
      }
    }
  },
  methods: {
    updateInfo(formName) {
      this.$refs[formName].validate((valide) => {
        if (valide) {
          axios.patch(`/myApp/users/`, this.centerForm).then(res => {
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
    cancel() {
      this.centerForm = this.$store.state.fisherman;
      console.log(this.$store.state.fisherman);
    }
  },
  created() {
    // console.log(this.$store.state.fisherman);
    this.centerForm = this.$store.state.fisherman;
  }
}
</script>

<style>
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
