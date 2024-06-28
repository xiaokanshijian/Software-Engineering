import { shallowMount } from '@vue/test-utils';
import BrushIcon from './BrushIcon.vue';





describe('<BrushIcon/>', () => {
	const wrapper = shallowMount(BrushIcon);

	// 快照测试
	it('snapshot测试', () => {
		const wrapper2 = shallowMount(BrushIcon);
		expect(wrapper2.html()).toMatchSnapshot()
		wrapper2.destroy()
    })

	
  });

