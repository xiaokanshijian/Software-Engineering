import { shallowMount } from '@vue/test-utils';
import LoopIcon from './LoopIcon.vue';





describe('<LoopIcon/>', () => {
	const wrapper = shallowMount(LoopIcon);

	// 快照测试
	it('snapshot测试', () => {
		const wrapper2 = shallowMount(LoopIcon);
		expect(wrapper2.html()).toMatchSnapshot()
		wrapper2.destroy()
    })

	
  });

