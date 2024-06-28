import { shallowMount } from '@vue/test-utils';
import SplitScreenIcon from './SplitScreenIcon.vue';





describe('<SplitScreenIcon/>', () => {
	const wrapper = shallowMount(SplitScreenIcon);

	// 快照测试
	it('snapshot测试', () => {
		const wrapper2 = shallowMount(SplitScreenIcon);
		expect(wrapper2.html()).toMatchSnapshot()
		wrapper2.destroy()
    })

	
  });

