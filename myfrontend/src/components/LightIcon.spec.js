import { shallowMount } from '@vue/test-utils';
import LightIcon from './LightIcon.vue';





describe('<LightIcon/>', () => {
	const wrapper = shallowMount(LightIcon);

	// 快照测试
	it('snapshot测试', () => {
		const wrapper2 = shallowMount(LightIcon);
		expect(wrapper2.html()).toMatchSnapshot()
		wrapper2.destroy()
    })

	
  });

