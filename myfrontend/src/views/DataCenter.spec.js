import { shallowMount } from '@vue/test-utils';
import DataCenter from './DataCenter.vue';





describe('<DataCenter/>', () => {
	const wrapper = shallowMount(DataCenter);

	// 快照测试
	it('snapshot测试', async () => {
		const wrapper2 = shallowMount(DataCenter);
		expect(wrapper2.html()).toMatchSnapshot()
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
