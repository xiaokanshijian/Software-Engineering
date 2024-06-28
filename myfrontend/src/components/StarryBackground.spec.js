import { shallowMount } from '@vue/test-utils';
import StarryBackground from './StarryBackground.vue';





describe('<StarryBackground/>', () => {
	const wrapper = shallowMount(StarryBackground);

	// 快照测试
	it('snapshot测试', () => {
		const wrapper2 = shallowMount(StarryBackground);
		expect(wrapper2.html()).toMatchSnapshot()
		wrapper2.destroy()
    })

	
  });

