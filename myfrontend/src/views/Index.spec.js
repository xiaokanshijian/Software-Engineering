import { shallowMount } from '@vue/test-utils';
import Index from './Index.vue';


beforeAll(() => {
  // 模拟BMap对象
  global.BMap = {
    // 添加你需要模拟的方法和属性
    Map: jest.fn().mockImplementation(() => ({
      addControl: jest.fn(),
      addOverlay: jest.fn(),
      // 其他需要模拟的BMap.Map方法
    })),
    // 其他需要模拟的BMap对象
  };
});


describe('<Index/>', () => {
	const wrapper = shallowMount(Index);

	// 快照测试
	it('snapshot测试', async () => { 
		const wrapper2 = shallowMount(Index);
		const result = await wrapper2.html()
		expect(result).toMatchSnapshot()
		wrapper2.destroy()
    })

	
  });

  /*
  it("slide correctly", () => {
		// 滑动 slide
		wrapper.find('slide-verification').trigger('check-result');
	  });
  		// 可以立即获取 msg 最新的值，不再需要 wrapper.vm.$nextTick();
		expect(wrapper.find('h1').text())
		  .toEqual('new message');
		  */
