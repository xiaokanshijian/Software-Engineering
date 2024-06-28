import { shallowMount } from '@vue/test-utils';
import LeftTop from './LeftTop.vue';





describe('<LeftTop/>', () => {
	const wrapper = shallowMount(LeftTop);

	// 快照测试
	it('snapshot测试', () => {
		const wrapper2 = shallowMount(LeftTop);
		expect(wrapper2.html()).toMatchSnapshot()
		wrapper2.destroy()
    })

	
  });

